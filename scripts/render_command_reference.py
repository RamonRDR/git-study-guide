"""Render canonical command catalog records as trilingual GitHub Markdown.

Stage the canonical JSON and curriculum changes first. The default is read-only
comparison; --write deliberately regenerates only the registered catalog pages.
"""
import argparse
from collections import Counter, defaultdict
from pathlib import PurePosixPath
from posixpath import relpath

import command_catalog as cc
from validate import ROOT, load_modules, navigation_entries, navigation_line, tracked_paths

LABELS = {
    "en": {
        "module": "15 Command Reference", "chapters": "Categories", "intent": "Find by intent",
        "intro": "Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.",
        "generated": "Generated from canonical catalog JSON. Edit the records, not this page.",
        "counts": "Counts by entry type", "purpose": "Purpose", "prerequisites": "Prerequisites",
        "options": "Options", "when_to_use": "When to use", "when_to_avoid": "When to avoid",
        "expected_state": "Expected result", "effect_notes": "Effects and side effects",
        "common_errors": "Common errors", "alternatives": "Alternatives", "recovery": "Recovery",
        "requirements": "Version and dependencies", "syntax": "Syntax", "basic": "Basic example",
        "professional": "Professional example", "risk": "Risk", "related": "Related lessons",
        "references": "Official documentation", "kind": "Type", "level": "Level",
        "effects": "State effects", "total": "Total distinct entries",
    },
    "pt-BR": {
        "module": "15 Referência de comandos", "chapters": "Categorias", "intent": "Pesquisar por intenção",
        "intro": "As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.",
        "generated": "Gerado a partir do JSON canônico. Edite os registros, não esta página.",
        "counts": "Quantidade por tipo de entrada", "purpose": "Finalidade", "prerequisites": "Pré-requisitos",
        "options": "Opções", "when_to_use": "Quando utilizar", "when_to_avoid": "Quando evitar",
        "expected_state": "Resultado esperado", "effect_notes": "Impactos e efeitos colaterais",
        "common_errors": "Erros comuns", "alternatives": "Alternativas", "recovery": "Recuperação",
        "requirements": "Versão e dependências", "syntax": "Sintaxe", "basic": "Exemplo básico",
        "professional": "Exemplo profissional", "risk": "Risco", "related": "Capítulos relacionados",
        "references": "Documentação oficial", "kind": "Tipo", "level": "Nível",
        "effects": "Impacto no estado", "total": "Total de entradas distintas",
    },
    "es": {
        "module": "15 Referencia de comandos", "chapters": "Categorías", "intent": "Buscar por intención",
        "intro": "Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.",
        "generated": "Generado a partir del JSON canónico. Edita los registros, no esta página.",
        "counts": "Cantidad por tipo de entrada", "purpose": "Finalidad", "prerequisites": "Requisitos previos",
        "options": "Opciones", "when_to_use": "Cuándo utilizar", "when_to_avoid": "Cuándo evitar",
        "expected_state": "Resultado esperado", "effect_notes": "Efectos y efectos secundarios",
        "common_errors": "Errores comunes", "alternatives": "Alternativas", "recovery": "Recuperación",
        "requirements": "Versión y dependencias", "syntax": "Sintaxis", "basic": "Ejemplo básico",
        "professional": "Ejemplo profesional", "risk": "Riesgo", "related": "Capítulos relacionados",
        "references": "Documentación oficial", "kind": "Tipo", "level": "Nivel",
        "effects": "Impacto en el estado", "total": "Total de entradas distintas",
    },
}

TERMS = {
    "native-command": ("Native command", "Comando nativo", "Comando nativo"),
    "subcommand": ("Subcommand", "Subcomando", "Subcomando"),
    "option-usage": ("Option usage", "Uso de opção", "Uso de opción"),
    "workflow": ("Workflow", "Fluxo", "Flujo"),
    "external-tool": ("External tool", "Ferramenta externa", "Herramienta externa"),
    "platform-operation": ("Platform operation", "Operação de plataforma", "Operación de plataforma"),
    "beginner": ("Beginner", "Iniciante", "Principiante"),
    "intermediate": ("Intermediate", "Intermediário", "Intermedio"),
    "advanced": ("Advanced", "Avançado", "Avanzado"),
    "read-only": ("Read-only", "Somente leitura", "Solo lectura"),
    "state-change": ("State change", "Alteração de estado", "Cambio de estado"),
    "destructive": ("Destructive", "Destrutivo", "Destructivo"),
    "history-rewrite": ("History rewrite", "Reescrita de histórico", "Reescritura del historial"),
    "remote-change": ("Remote change", "Alteração remota", "Cambio remoto"),
    "sensitive": ("Sensitive", "Sensível", "Sensible"),
    "unchanged": ("Unchanged", "Inalterado", "Sin cambios"),
    "changes": ("Changes", "Altera", "Cambia"),
    "conditional": ("Conditional", "Condicional", "Condicional"),
    "not-applicable": ("Not applicable", "Não se aplica", "No aplica"),
    "working_tree": ("Working tree", "Working tree", "Working tree"),
    "index": ("Index", "Index", "Index"),
    "history": ("Objects / refs / history", "Objetos / refs / histórico", "Objetos / refs / historial"),
    "remote": ("Remote repository", "Repositório remoto", "Repositorio remoto"),
    "other": ("Other state", "Outros estados", "Otros estados"),
}

EFFECT_ORDER = ("working_tree", "index", "history", "remote", "other")
BEFORE_EXAMPLES = ("purpose", "prerequisites", "options", "when_to_use", "when_to_avoid")
AFTER_EXAMPLES = ("expected_state", "effect_notes", "common_errors", "alternatives", "recovery", "requirements")

def term(key, locale):
    return TERMS[key][cc.LOCALES.index(locale)]

def filename(locale):
    return "README" + cc.SUFFIX[locale] + ".md"

def relative(source, target):
    return relpath(target, str(PurePosixPath(source).parent))

def nav_block(name, line):
    return f"<!-- {name} -->\n{line}\n<!-- /{name} -->"

def header(title, document, entries):
    selector = " · ".join(f"[{label}]({filename(locale)})" for label, locale in zip(
        ("English", "Português", "Español"), cc.LOCALES))
    return [f"# {title}", "", selector, "", nav_block("navigation", navigation_line(document, entries)), ""]

def footer(document, entries):
    return ["", "---", "", nav_block("navigation-footer", navigation_line(document, entries)), ""]

def md_text(value):
    # Render plain localized prose without letting it introduce Markdown structure.
    return "".join("\\" + ch if ch in "\\\x60*_[]|~" else ch for ch in value)

def code(value):
    return "\x60" + value + "\x60"

def field(lines, label, text):
    lines.extend([f"**{label}:** {md_text(text)}", ""])

def entry_lines(entry, locale, document, intents):
    labels = LABELS[locale]
    lines = [f"## {entry['id']}", "", f"**{code(entry['command'])}**", ""]
    field(lines, labels["kind"], term(entry["kind"], locale))
    field(lines, labels["level"], term(entry["level"], locale))
    field(lines, labels["intent"], ", ".join(intents[tag][locale] for tag in entry["intent_tags"]))
    field(lines, labels["risk"], term(entry["risk"]["class"], locale) + ". " + entry["risk"]["notes"][locale])
    for key in BEFORE_EXAMPLES:
        field(lines, labels[key], entry[key][locale])
    lines.extend([f"**{labels['syntax']}**", "", code(entry["syntax"]), ""])
    for key in ("basic", "professional"):
        example = entry["examples"][key]
        lines.extend([f"**{labels[key]}**", "", code(example["command"]), "", md_text(example["context"][locale]), ""])
    lines.extend([f"**{labels['effects']}**", ""])
    for key in EFFECT_ORDER:
        lines.append(f"- {term(key, locale)}: {term(entry['effects'][key], locale)}")
    lines.append("")
    for key in AFTER_EXAMPLES:
        field(lines, labels[key], entry[key][locale])
    lines.extend([f"**{labels['related']}**", ""])
    for chapter in entry["related_chapters"]:
        target = chapter + "/" + filename(locale)
        lines.append(f"- [{chapter}]({relative(document, target)})")
    lines.extend(["", f"**{labels['references']}**", ""])
    for url in entry["references"]:
        lines.append(f"- <{url}>")
    lines.append("")
    return lines

def render_category(item, records, locale, document, nav, intents):
    labels = LABELS[locale]
    lines = header(item["slug"][:2] + " " + md_text(item["title"][locale]), document, nav)
    lines.extend([labels["generated"], "", labels["intro"], "", f"**{labels['total']}: {len(records)}**", ""])
    for entry in records:
        lines.append(f"- [{code(entry['command'])}](#{entry['id']})")
    lines.append("")
    for entry in records:
        lines.extend(entry_lines(entry, locale, document, intents))
    return "\n".join(lines + footer(document, nav))

def render_index(grouped, locale, document, nav, intents):
    labels = LABELS[locale]
    lines = header(labels["module"], document, nav)
    entries = [entry for _, records in grouped for entry in records]
    lines.extend([labels["generated"], "", labels["intro"], "", f"**{labels['total']}: {len(entries)}**", "",
                  f"## {labels['chapters']}", "", "<!-- chapters -->"])
    for item, records in grouped:
        lines.append(f"- [{md_text(item['title'][locale])}]({item['slug']}/{filename(locale)}) ({len(records)})")
    lines.extend(["<!-- /chapters -->", "", f"## {labels['counts']}", ""])
    counts = Counter(e["kind"] for e in entries)
    for kind in sorted(cc.KINDS):
        lines.append(f"- {term(kind, locale)}: {counts[kind]}")
    lines.extend(["", f"## {labels['intent']}", ""])
    by_intent = defaultdict(list)
    for item, records in grouped:
        for entry in records:
            for tag in entry["intent_tags"]:
                by_intent[tag].append((item, entry))
    for tag in sorted(by_intent):
        lines.extend([f"### {md_text(intents[tag][locale])}", ""])
        for item, entry in by_intent[tag]:
            lines.append(f"- [{code(entry['command'])}]({item['slug']}/{filename(locale)}#{entry['id']})")
        lines.append("")
    return "\n".join(lines + footer(document, nav))

def render_all(grouped, modules, intents):
    output = {}
    for locale in cc.LOCALES:
        navigation = {doc: nav for doc, nav, _ in navigation_entries(modules, cc.SUFFIX[locale])}
        document = cc.MODULE + "/" + filename(locale)
        output[document] = render_index(grouped, locale, document, navigation[document], intents)
        for item, records in grouped:
            document = f"{cc.MODULE}/{item['slug']}/{filename(locale)}"
            output[document] = render_category(item, records, locale, document, navigation[document], intents)
    return output

def compare_generated(root, paths, output):
    errors = []
    for path, expected in sorted(output.items()):
        if path not in paths or not (root / path).is_file():
            errors.append("Missing generated catalog page: " + path)
        elif (root / path).read_text(encoding="utf-8") != expected:
            errors.append("Stale generated catalog page: " + path)
    return errors

def check_catalog(root, paths):
    try:
        modules = load_modules(root)
        grouped = cc.load_catalog(root, paths, modules)
        return compare_generated(root, paths, render_all(grouped, modules, cc.intents(root)))
    except (OSError, ValueError, TypeError, KeyError, StopIteration) as exc:
        return ["Invalid command catalog: " + str(exc)]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate catalog Markdown")
    args = parser.parse_args()
    paths = tracked_paths(ROOT)
    modules = load_modules(ROOT)
    grouped = cc.load_catalog(ROOT, paths, modules)
    output = render_all(grouped, modules, cc.intents(ROOT))
    if args.write:
        for path, content in sorted(output.items()):
            target = ROOT / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")
        print(f"Generated {len(output)} Markdown pages")
        return 0
    errors = compare_generated(ROOT, paths, output)
    for error in errors:
        print(error)
    return int(bool(errors))

if __name__ == "__main__":
    raise SystemExit(main())
