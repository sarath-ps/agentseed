# Living Specs

Capability-based specifications live here.

Each capability has its own folder containing a `spec.md` file written in Markdown with:

- Requirements ("The system SHALL...")
- Scenarios (GIVEN / WHEN / THEN)

Example structure:

```
specs/
├── auth-session/
│   └── spec.md
├── checkout-cart/
│   └── spec.md
└── ...
```

These are the source of truth. Changes propose deltas that are later archived back into these files.
