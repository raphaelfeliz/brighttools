

// Add-on Logic
const addonList = document.getElementById('addon-list');
const selectedAddons = {}; // { "Product Name": { qty: 1, price: 24.95 } }

function addToCart(btn) {
    const icon = btn.querySelector('i');
    const isAdded = btn.classList.contains('bg-green-500');

    // Find product details
    const productCard = btn.closest('.group');
    const productName = productCard.querySelector('h3').innerText;
    const priceText = productCard.querySelector('p').innerText;
    const price = parseFloat(priceText.replace('$', ''));

    if (!isAdded) {
        // Add item (initial add)
        btn.classList.remove('bg-white', 'text-slate-900', 'hover:bg-red-600', 'hover:text-white');
        btn.classList.add('bg-green-500', 'text-white');
        icon.className = 'fa-solid fa-check';

        if (!selectedAddons[productName]) {
            selectedAddons[productName] = { qty: 1, price: price };
        }
    } else {
        // Remove item (toggle off)
        btn.classList.add('bg-white', 'text-slate-900', 'hover:bg-red-600', 'hover:text-white');
        btn.classList.remove('bg-green-500', 'text-white');
        icon.className = 'fa-solid fa-plus';

        delete selectedAddons[productName];
    }

    renderAddons();
}

function updateQuantity(productName, change) {
    if (selectedAddons[productName]) {
        selectedAddons[productName].qty += change;

        // If quantity goes to 0, remove the item and reset the button
        if (selectedAddons[productName].qty <= 0) {
            delete selectedAddons[productName];

            // Find and reset the button
            const allCards = document.querySelectorAll('#related-products .group');
            allCards.forEach(card => {
                if (card.querySelector('h3').innerText === productName) {
                    const btn = card.querySelector('button');
                    const icon = btn.querySelector('i');
                    btn.classList.add('bg-white', 'text-slate-900', 'hover:bg-red-600', 'hover:text-white');
                    btn.classList.remove('bg-green-500', 'text-white');
                    icon.className = 'fa-solid fa-plus';
                }
            });
        }
    }
    renderAddons();
}

function renderAddons() {
    addonList.innerHTML = '';
    const items = Object.keys(selectedAddons);

    if (items.length > 0) {
        addonList.classList.remove('hidden');
        items.forEach(item => {
            const data = selectedAddons[item];
            const totalItemPrice = (data.price * data.qty).toFixed(2);

            const div = document.createElement('div');
            div.className = 'flex justify-between items-center bg-white p-3 rounded-lg border border-slate-100 shadow-sm';
            div.innerHTML = `
                            <div class="flex items-center gap-3">
                                <div class="flex items-center border border-slate-200 rounded-md overflow-hidden">
                                    <button onclick="updateQuantity('${item}', -1)" class="px-2 py-1 bg-slate-50 hover:bg-slate-100 text-slate-600 transition">-</button>
                                    <span class="px-2 py-1 text-sm font-bold text-slate-900 min-w-[1.5rem] text-center bg-white">${data.qty}</span>
                                    <button onclick="updateQuantity('${item}', 1)" class="px-2 py-1 bg-slate-50 hover:bg-slate-100 text-slate-600 transition">+</button>
                                </div>
                                <span class="font-medium text-slate-700">${item}</span>
                            </div>
                            <span class="text-sm font-bold text-slate-900">$${totalItemPrice}</span>
                        `;
            addonList.appendChild(div);
        });
    } else {
        addonList.classList.add('hidden');
    }
}

// Carousel Logic
let currentSlide = 0;
const carouselTrack = document.getElementById('info-carousel');
const dots = document.querySelectorAll('.carousel-dot');
const totalSlides = carouselTrack.children.length;
let slideInterval;

function setSlide(index, autoPlay = true) {
    currentSlide = index;
    updateCarousel();
    if (autoPlay) {
        resetInterval();
    } else {
        clearInterval(slideInterval);
    }
}

function updateCarousel() {
    const translateX = -(currentSlide * 100);
    carouselTrack.style.transform = `translateX(${translateX}%)`;

    // Update dots
    dots.forEach((dot, idx) => {
        if (idx === currentSlide) {
            dot.classList.remove('bg-slate-300');
            dot.classList.add('bg-red-600');
        } else {
            dot.classList.remove('bg-red-600');
            dot.classList.add('bg-slate-300');
        }
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateCarousel();
}

function resetInterval() {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, 5000); // Auto-slide every 5 seconds
}

function pauseAutoSlide() {
    clearInterval(slideInterval);
}

// Expose API for Tour
window.CaravanCarousel = {
    goToSlide: setSlide,
    pause: pauseAutoSlide,
    resume: resetInterval
};

// Start auto-slide
resetInterval();
