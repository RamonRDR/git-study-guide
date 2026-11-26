# YAML and configuration reading

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-ci-delivery-and-deployment/README.md) · [Index](../README.md) · [Next](../03-github-actions/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [Integration, delivery and deployment](../01-ci-delivery-and-deployment/README.md)

**Objective:** Read mappings, sequences, scalars and multiline commands before editing automation.

## What and why

YAML is a data serialization format; a platform assigns meaning to its keys. A mapping pairs keys and values; a sequence uses hyphens; scalars represent individual values. Indent consistently with spaces, never tabs for indentation. Quote strings when punctuation or implicit types could be ambiguous. A block scalar `|` preserves line breaks, while `>` folds many line breaks into spaces. Duplicate keys and incorrect nesting are defects even if a permissive parser accepts them. YAML versions/parsers can interpret plain words differently; GitHub's workflow key `on` is valid on GitHub, but a YAML 1.1 parser may interpret it as a boolean. A syntactically valid file can still violate a platform schema.

```yaml
project:
  name: "catalog"
  attempts: 2
  tasks:
    - check
    - report
  message: |
    First line
    Second line
```

## Practice

Offline, inspect the neutral example below. Find one mapping, one list, a string and an integer; explain why `check` belongs to `tasks`. Then draw the tree before and after mistakenly unindenting `tasks`. This is data only, not a CI configuration.

## Common mistakes and safety

Never paste secrets into YAML. Validate with the target platform's schema, not merely a generic parser; no external editor is required. Inspect the diff and correct indentation in a disposable copy.

## Exercise and self-check

`project` contains a mapping; `tasks` contains a sequence; `check` is a list item; `attempts` is an integer. Pass if you distinguish syntax from platform semantics.

## Quick reference

mapping / sequence / scalar

## Official sources

- <https://yaml.org/spec/1.2.2/>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/>
