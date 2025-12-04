# Master Plan: Page Improvements & Persuasion Tour

This document outlines the roadmap for adding new features to the landing page and implementing an interactive "Persuasion Tour" to showcase the marketing psychology behind the design.

## Phase 1: New Feature Implementation (Related Products)
**Goal**: Increase Average Order Value (AOV) by offering relevant add-ons.

### 1. Related Products Carousel
Implement a responsive carousel section (likely placed before the footer) featuring the following items:
*   **High-reach van cleaner**
*   **Quick mop microfiber**
*   **Floor Wipes for Wooden Floors Poliwix**
*   **Stainless Steel Telescopic Handle**

**Functional Requirements:**
*   **Multi-Add Capability**: Users can add multiple different items without page reload.
*   **Instant Feedback**: Clicking "Add" triggers an immediate visual success state (e.g., button turns green/says "Added", or a small toast notification).
*   **Layout**: Horizontal scroll (carousel) on mobile, grid or carousel on desktop depending on width.

## Phase 2: Persuasion Tour (Onboarding Mode)
**Goal**: Create an interactive overlay that guides the viewer through the psychological triggers used on the page.

### Technical Strategy
*   **Overlay**: Dark semi-transparent backdrop.
*   **Spotlight**: Highlights specific DOM elements.
*   **Navigation**: "Next/Prev" controls to move between points.

### Tour Points (The Script)

#### 1. The "Sum of Parts" Value (User Request)
*   **Target**: The "What's Included" Grid (specifically pointing to a single card like the Broom).
*   **Insight**: "Individual Value Anchoring. Instead of just listing items, we give each product its own 'hero' card with features. This establishes that the bundle is made of high-value, standalone tools, making the total package price feel like a steal."

#### 2. Frictionless Cross-Sells (User Request)
*   **Target**: The new "Related Products" Carousel.
*   **Insight**: "One-Click Upsells. By allowing users to 'toss' extra items into the cart with a single click (and instant feedback), we reduce the friction of decision-making and increase Average Order Value."

#### 3. Authority & Trust
*   **Target**: "2-Year Warranty" Badge (Hero Section).
*   **Insight**: "Trust Signals. Addressing durability concerns upfront builds confidence before the pitch begins."

#### 4. Benefit-Driven Headline
*   **Target**: Main Headline ("The Ultimate...").
*   **Insight**: "Value Proposition. We focus on the *result* (Ultimate Clean) rather than just the product name."

#### 5. Social Proof
*   **Target**: "Star Item" Badge (Broom Card).
*   **Insight**: "Guided Choice. Labeling a 'Star Item' creates a focal point and implies popularity/validation by other customers."

#### 6. Scarcity & Urgency
*   **Target**: "In Stock" Indicator.
*   **Insight**: "Availability Heuristic. Green 'In Stock' lights signal readiness but also subtle urgency—it's here *now*, but maybe not later."

#### 7. Reciprocity
*   **Target**: "Complimentary" Travel Bag.
*   **Insight**: "Perceived Value. Giving a 'free' gift triggers the reciprocity effect and increases the tangible value of the offer."

#### 8. Risk Reversal
*   **Target**: "Peace of Mind Guarantee" (Footer).
*   **Insight**: "Risk Reversal. A bold guarantee removes the fear of buyer's remorse, often the final barrier to conversion."

## Phase 3: Execution Steps
1.  **Update HTML Structure**: Add `id` attributes to all target elements for the tour.
2.  **Build Carousel**: Code the HTML/CSS/JS for the Related Products section.
3.  **Build Tour Engine**: Implement the JS logic for the overlay and step navigation.
4.  **Launch**: Add the "Analyze Page Strategy" trigger button.