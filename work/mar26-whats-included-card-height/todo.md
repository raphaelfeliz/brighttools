# Work Package: Reduce What's Included Card Height & Even Spacing (`todo.md`)

## File Versioning
- **Target Section**: `sections/mar26-whats-included.liquid`
- **Target Documentation**: `docs/documentation/sections/mar26-whats-included.md`

---

## Action Checklist

- [x] **Task 1: Remove Card Description HTML, CSS & Schema Setting**
  - Deleted `<div class="mar26-included-card-desc">` from meta-items loop and block loop in `sections/mar26-whats-included.liquid`.
  - Deleted `.mar26-included-card-desc` CSS rule block.
  - Deleted `"description"` rich-text setting from block schema to clean up Theme Editor sidebar.

- [x] **Task 2: Remove Specs Divider Line & Standardize Gaps**
  - Set `border-top: none;` and `padding-top: 0;` on `.mar26-included-card-specs` in `sections/mar26-whats-included.liquid`.
  - Set specs item `gap: 0.375rem` (20% tighter vertical rhythm).

- [x] **Task 3: Implement Even Vertical Spacing & Version Bump to 1.5.0**
  - Set image padding to `1rem 1rem 0.75rem 1rem`.
  - Set card body padding to `0.75rem 1.25rem 1rem 1.25rem`.
  - Bumped version to `1.5.0 - Even Vertical Spacing & Compact Layout`.

- [x] **Task 4: Update Documentation**
  - Updated `docs/documentation/sections/mar26-whats-included.md` for Version 1.5.0.

- [x] **Task 5: Generate Handover**
  - Created complete handover report in `handover.md`.
