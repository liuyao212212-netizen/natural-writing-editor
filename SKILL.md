---
name: natural-writing-editor
description: Edit Chinese or English drafts into clear, natural, specific writing while preserving the author's meaning, facts, and personal voice. Use when an AI agent needs to polish a message, article, report, application, social post, product copy, or bilingual draft; reduce formulaic AI-like phrasing; match a supplied voice sample; or audit prose for vague, inflated, repetitive, and overly structured language.
---

# Natural Writing Editor

Improve writing for humans, not for detector evasion. Preserve intent and facts; make every substantial change explainable.

## Workflow

1. Identify audience, channel, purpose, language, and desired intensity. Choose light polish, deep rewrite, voice match, or factual copy edit. See [editing-modes.md](references/editing-modes.md).
2. Lock facts, names, numbers, citations, commitments, and quotations. Do not silently change them.
3. If voice matching, extract 3–7 observable traits from samples and fill [voice-profile-template.md](assets/voice-profile-template.md). Do not imitate living authors on request; use high-level traits instead.
4. Audit the draft with `python scripts/style_audit.py draft.txt --format markdown`. Treat findings as prompts for judgment, not automatic proof.
5. Rewrite for concrete nouns and verbs, varied rhythm, honest confidence, direct attribution, and channel-appropriate length. For Chinese patterns, read [chinese-patterns.md](references/chinese-patterns.md).
6. Compare the revision against the locked facts and original intent.
7. Return the revised text first. Add a short change note only when useful or requested.

## Guardrails

- Never fabricate examples, sources, personal experience, metrics, or certainty.
- Do not optimize for bypassing AI detectors or disguising authorship.
- Preserve meaningful quirks unless they block comprehension.
- Ask before changing legal, medical, financial, contractual, or reputational claims.
- Prefer a few precise changes over decorative rewriting.
