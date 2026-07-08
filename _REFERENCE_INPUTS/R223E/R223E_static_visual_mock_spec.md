# R223E Static Visual Mock Spec

```text
stage_id=1013R_R223E_STATIC_VISUAL_MOCK_FIXTURE
status=static_visual_mock_only
ui_implementation=false
R97B_modified=false
frontend_backend_modified=false
runtime_enabled=false
formal_apply=false
```

## Purpose

R223E moves from text-only density rules to a static visual mock fixture. It tests whether the minimum workbench can remain readable when the prep canvas, focused section, component strip, source/gap rail, binding preview, quick mode block, and bottom local note input are shown together.

## Static Mock Scope

Allowed:

- static HTML fixture;
- screenshot smoke;
- file-level density compliance check;
- review ZIP.

Blocked:

- no R97B route;
- no official frontend/backend change;
- no runtime/provider/model/prompt/db;
- no real component interaction;
- no formal apply.

## Visual Decisions Reflected

1. The prep canvas remains the primary reading object.
2. The current focused section is visually highlighted.
3. Ordinary gaps and assumptions are folded; high-risk confirmation remains visible.
4. Daily mode shows exactly 3 recommended components for the focused section.
5. Quick mode shows exactly 2 recommended components.
6. Binding preview shows selected component only.
7. Bottom input has low visual weight and local-note wording.
8. No 12-component shelf appears.
9. No chat-style prompt appears.

## Review Question

Does the static mock look like a constrained teaching workbench rather than a chat tool or component marketplace?
