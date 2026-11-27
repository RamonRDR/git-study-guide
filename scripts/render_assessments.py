"""Deterministic Markdown for the internal Sprint 17 assessment pilot."""
import argparse
from pathlib import Path
from posixpath import relpath, dirname

if __package__:
    from .assessment_pilot import BANKS, LOCALES, load_assessments
    from .validate import load_modules, navigation_entries, navigation_line, tracked_paths, read_text
else:
    from assessment_pilot import BANKS, LOCALES, load_assessments
    from validate import load_modules, navigation_entries, navigation_line, tracked_paths, read_text

SUFFIX = {"en": "", "pt-BR": ".pt-BR", "es": ".es"}
TITLES = {
    "en": ("17 Challenges & Interviews", "Quizzes", "Practical challenges", "Interview questions", "Mock assessments"),
    "pt-BR": ("17 Desafios e entrevistas", "Quizzes", "Desafios práticos", "Perguntas de entrevista", "Simulados"),
    "es": ("17 Desafíos y entrevistas", "Cuestionarios", "Desafíos prácticos", "Preguntas de entrevista", "Simulacros"),
}
LABELS = {
    "en": ("Chapters", "Difficulty", "Prerequisites", "Hints", "Answer", "Explanation", "Setup", "Solution",
           "State checks", "Execution", "Time (min)", "Expected answer", "Rubric", "Follow-ups", "Included records"),
    "pt-BR": ("Capítulos", "Dificuldade", "Pré-requisitos", "Dicas", "Resposta", "Explicação", "Preparação", "Solução",
              "Checks de estado", "Execução", "Tempo (min)", "Resposta esperada", "Rubrica", "Complementos", "Registros incluídos"),
    "es": ("Capítulos", "Dificultad", "Prerrequisitos", "Pistas", "Respuesta", "Explicación", "Preparación", "Solución",
           "Checks de estado", "Ejecución", "Tiempo (min)", "Respuesta esperada", "Rúbrica", "Seguimiento", "Registros incluidos"),
}
INTRO = {
    "en": "Try first, consult the public solutions afterward. Quizzes use exact choices; interviews and mocks require honest self-assessment. Challenges use only fresh disposable local repositories and fixed state checks, not automatic execution of learner commands. All records form an internal pilot, not the final Learning Hub contract.",
    "pt-BR": "Tente primeiro, consulte as soluções públicas depois. Quizzes usam escolhas exatas; entrevistas e simulados exigem autoavaliação honesta. Desafios usam somente repositórios locais descartáveis novos e checks fixos de estado, sem executar automaticamente comandos de alunos. Registros são piloto interno, não contrato final do Learning Hub.",
    "es": "Intenta primero, consulta las soluciones públicas después. Cuestionarios usan opciones exactas; entrevistas y simulacros requieren autoevaluación honesta. Desafíos usan solo repositorios locales desechables nuevos y checks fijos de estado, sin ejecutar automáticamente comandos de estudiantes. Registros son piloto interno, no contrato final de Learning Hub.",
}
DIFFICULTY = {"en": ("easy", "medium", "hard"), "pt-BR": ("fácil", "médio", "difícil"),
              "es": ("fácil", "medio", "difícil")}

def md(value):
    return "".join("\\" + c if c in "\\*_[]|~" or c == chr(96) else c for c in value)

def filename(locale):
    return "README" + SUFFIX[locale] + ".md"

def nav_block(name, line):
    return ["<!-- " + name + " -->", line, "<!-- /" + name + " -->"]

def render_page(title, document, entries, body):
    nav = navigation_line(document, entries)
    return "\n".join(["# " + title, "", "[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)", "",
                     *nav_block("navigation", nav), "", *body, "", "---", "", *nav_block("navigation-footer", nav), ""])

def render_records(records, kind, locale, document):
    labels = LABELS[locale]
    result = [INTRO[locale], ""]
    def field(label, value):
        result.extend(["**" + label + ":** " + value, ""])
    def listing(label, values):
        result.extend(["**" + label + ":**", "", *("- " + md(v[locale]) for v in values), ""])
    for record in records:
        result.extend(["## " + md(record["title"][locale]), "", "ID: " + record["id"], ""])
        field(labels[1], DIFFICULTY[locale][("easy", "medium", "hard").index(record["difficulty"])])
        field(labels[2], " · ".join("[" + p + "](" + relpath(p + "/" + filename(locale), dirname(document)) + ")"
                                  for p in record["prerequisites"]))
        result.extend([md(record["prompt"][locale]), ""])
        if kind == "quiz":
            result.extend([*("- " + c["id"] + ". " + md(c["text"][locale]) for c in record["choices"]), ""])
        if kind == "challenge":
            field(labels[10], str(record["estimated_minutes"]))
            field(labels[9], "local_only · " + md(record["execution_reason"][locale]))
            field(labels[6], md(record["setup"][locale]))
        if kind == "mock":
            field(labels[10], str(record["duration_minutes"]))
            field(labels[14], ", ".join(record["quiz_ids"] + record["challenge_ids"] + record["interview_ids"]))
        listing(labels[3], record["hints"])
        if kind == "quiz":
            field(labels[4], record["answer"])
        elif kind == "challenge":
            listing(labels[7], record["solution"])
            result.extend(["**" + labels[8] + ":**", ""])
            for check in record["checks"]:
                result.append("- " + md(", ".join(k + "=" + str(v) for k, v in sorted(check.items()))))
            result.append("")
        elif kind == "interview":
            field(labels[11], md(record["expected_answer"][locale]))
            listing(labels[12], record["rubric"])
            listing(labels[13], record["follow_ups"])
        else:
            listing(labels[12], record["rubric"])
        field(labels[5], md(record["explanation"][locale]))
    return result[:-1]

def render_all(grouped, modules):
    output = {}
    for locale in LOCALES:
        f = filename(locale)
        nav = {p: entries for p, entries, _ in navigation_entries(modules, SUFFIX[locale])}
        index = "exercises/" + f
        titles = TITLES[locale]
        body = [INTRO[locale], "", "## " + LABELS[locale][0], "", "<!-- chapters -->",
                *("- [" + title + "](" + slug + "/" + f + ")" for slug, title in zip(BANKS, titles[1:])),
                "<!-- /chapters -->"]
        output[index] = render_page(titles[0], index, nav[index], body)
        for slug, title in zip(BANKS, titles[1:]):
            document = "exercises/" + slug + "/" + f
            output[document] = render_page(title, document, nav[document],
                                           render_records(grouped[slug], BANKS[slug], locale, document))
    return output

def check_assessments(root, paths):
    try:
        modules = load_modules(root)
        output = render_all(load_assessments(root, paths, modules), modules)
        return ["Assessment Markdown mismatch: " + p for p, value in output.items()
                if p not in paths or read_text(root, p) != value]
    except (ValueError, OSError, TypeError, KeyError, StopIteration) as exc:
        return ["Invalid assessment pilot: " + str(exc)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    paths = tracked_paths(root)
    if not args.write:
        errors = check_assessments(root, paths)
        for error in errors:
            print(error)
        return int(bool(errors))
    modules = load_modules(root)
    for path, value in render_all(load_assessments(root, paths, modules), modules).items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value, encoding="utf-8", newline="\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
