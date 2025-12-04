const tourSteps = [
    {
        element: '#tour-warranty',
        title: 'Trust Signals',
        description: 'Immediately addressing anxiety about product durability builds confidence before the user even reads the details. The "2-Year Warranty" badge is placed at the very top to disarm skepticism.'
    },
    {
        element: '#tour-headline',
        title: 'Value Proposition',
        description: 'We focus on the *result* ("Ultimate Clean") rather than just the product name. The word "Ultimate" is highlighted to frame this as the best-in-class solution.'
    },
    {
        element: '#tour-cta',
        title: 'Direct Action',
        description: 'High-contrast buttons with clear, action-oriented text ("Get", "Buy") reduce friction. The shadow and hover effects make it feel clickable and tangible.'
    },
    {
        element: '#tour-social-proof',
        title: 'Social Proof & Guidance',
        description: 'Labeling a "Star Item" creates a focal point. It implies popularity and guides the user\'s attention to the core value proposition (the Broom) first.'
    },
    {
        element: '#tour-stock',
        title: 'Scarcity & Urgency',
        description: 'The green "In Stock" indicator signals readiness but also implies that availability could change. It encourages faster decision-making without being aggressive.'
    },
    {
        element: '#tour-value',
        title: 'Perceived Value (Reciprocity)',
        description: 'Giving a "Complimentary" gift (the bag) triggers the reciprocity effect. It increases the bundle\'s perceived worth without significantly increasing the cost to the user.'
    },
    {
        element: '#related-products',
        title: 'Frictionless Cross-Sells',
        description: 'One-Click Upsells. By allowing users to "toss" extra items into the cart with a single click (and instant feedback), we reduce the friction of decision-making and increase Average Order Value.'
    },
    {
        element: '#tour-guarantee',
        title: 'Risk Reversal',
        description: 'A bold guarantee removes the fear of buyer\'s remorse. Placing it near the final call-to-action acts as a safety net for the purchase decision.'
    }
];

class Tour {
    constructor(steps) {
        this.steps = steps;
        this.currentStep = 0;
        this.isActive = false;

        this.init();
    }

    init() {
        // Create UI elements
        this.createOverlay();
        this.createTooltip();
        this.createTrigger();

        // Bind events
        window.addEventListener('resize', () => {
            if (this.isActive) this.positionTooltip();
        });
    }

    createOverlay() {
        this.overlay = document.createElement('div');
        this.overlay.id = 'tour-overlay';
        document.body.appendChild(this.overlay);
    }

    createTooltip() {
        this.tooltip = document.createElement('div');
        this.tooltip.id = 'tour-tooltip';
        this.tooltip.innerHTML = `
            <div class="tour-close"><i class="fa-solid fa-times"></i></div>
            <h3 id="tour-title"></h3>
            <p id="tour-desc"></p>
            <div class="tour-nav">
                <button class="tour-btn tour-btn-prev">Previous</button>
                <span id="tour-progress" class="text-xs text-slate-500"></span>
                <button class="tour-btn tour-btn-next">Next</button>
            </div>
        `;
        document.body.appendChild(this.tooltip);

        // Event listeners
        this.tooltip.querySelector('.tour-btn-next').addEventListener('click', () => this.nextStep());
        this.tooltip.querySelector('.tour-btn-prev').addEventListener('click', () => this.prevStep());
        this.tooltip.querySelector('.tour-close').addEventListener('click', () => this.endTour());
    }

    createTrigger() {
        const btn = document.createElement('div');
        btn.id = 'tour-trigger';
        btn.innerHTML = '<i class="fa-solid fa-magnifying-glass-chart"></i> Analyze Page Strategy';
        btn.addEventListener('click', () => this.startTour());
        document.body.appendChild(btn);
    }

    startTour() {
        this.isActive = true;
        this.currentStep = 0;
        this.overlay.classList.add('active');
        this.showStep(0);
    }

    endTour() {
        this.isActive = false;
        this.overlay.classList.remove('active');
        this.tooltip.classList.remove('active');
        this.removeHighlight();
    }

    removeHighlight() {
        const highlighted = document.querySelector('.tour-highlight');
        if (highlighted) {
            highlighted.classList.remove('tour-highlight');
        }
    }

    showStep(index) {
        if (index < 0 || index >= this.steps.length) return;

        this.removeHighlight();
        this.currentStep = index;

        const step = this.steps[index];
        const element = document.querySelector(step.element);

        if (element) {
            // Scroll to element
            element.scrollIntoView({ behavior: 'smooth', block: 'center' });

            // Highlight element
            // We use a timeout to wait for scroll to finish/start
            setTimeout(() => {
                element.classList.add('tour-highlight');
                this.updateTooltipContent(step);
                this.positionTooltip(element);
                this.tooltip.classList.add('active');
            }, 300);
        }
    }

    updateTooltipContent(step) {
        document.getElementById('tour-title').textContent = step.title;
        document.getElementById('tour-desc').textContent = step.description;
        document.getElementById('tour-progress').textContent = `${this.currentStep + 1} / ${this.steps.length}`;

        const prevBtn = this.tooltip.querySelector('.tour-btn-prev');
        const nextBtn = this.tooltip.querySelector('.tour-btn-next');

        prevBtn.style.visibility = this.currentStep === 0 ? 'hidden' : 'visible';
        nextBtn.textContent = this.currentStep === this.steps.length - 1 ? 'Finish' : 'Next';
    }

    positionTooltip(targetElement) {
        if (!targetElement) targetElement = document.querySelector(this.steps[this.currentStep].element);

        const rect = targetElement.getBoundingClientRect();
        const tooltipRect = this.tooltip.getBoundingClientRect();

        // Default position: Bottom
        let top = rect.bottom + 15 + window.scrollY;
        let left = rect.left + (rect.width / 2) - (tooltipRect.width / 2) + window.scrollX;

        // Check if off-screen (right)
        if (left + tooltipRect.width > window.innerWidth) {
            left = window.innerWidth - tooltipRect.width - 20;
        }
        // Check if off-screen (left)
        if (left < 20) {
            left = 20;
        }

        // Check if off-screen (bottom) - flip to top
        if (rect.bottom + tooltipRect.height + 20 > window.innerHeight + window.scrollY) {
            top = rect.top - tooltipRect.height - 15 + window.scrollY;
        }

        this.tooltip.style.top = `${top}px`;
        this.tooltip.style.left = `${left}px`;
    }

    nextStep() {
        if (this.currentStep < this.steps.length - 1) {
            this.showStep(this.currentStep + 1);
        } else {
            this.endTour();
        }
    }

    prevStep() {
        if (this.currentStep > 0) {
            this.showStep(this.currentStep - 1);
        }
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    new Tour(tourSteps);
});
