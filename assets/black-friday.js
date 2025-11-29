// 🚀 @raphael.feliz - START BLACK FRIDAY INJECTION SCRIPT (Announcement Bar Only v3.5) 🚀
(function() {
    // ==========================================
    // ⚙️ CONFIGURATION
    // ==========================================
    const BF_VERSION = "v3.5 (Announcement Bar Only)"; 
    const BF_STATUS = "test"; // Options: "test" (requires ?test=bf URL) | "live" (visible to everyone)
    
    const CONFIG = {
        RED_PRIMARY: "#D4212C",
        RED_DARK: "#B91C24",
        YELLOW_GLOW: "#FFD700",
        GREEN_GLOW: "#3CB371",
        IDS: {
            ANNOUNCEMENT_BAR: "shopify-section-sections--24966839730450__announcement-bar"
        }
    };

    // ==========================================
    // 🕵️ STATUS CHECK
    // ==========================================
    console.log(`%c BF Script ${BF_VERSION}: Status [${BF_STATUS.toUpperCase()}]`, "background: #D4212C; color: #fff; font-weight: bold; padding: 4px 8px; font-size: 12px;");

    const urlParams = new URLSearchParams(window.location.search);
    const isTestUrl = urlParams.has('test') && urlParams.get('test') === 'bf';
    const shouldRun = (BF_STATUS === 'live') || (BF_STATUS === 'test' && isTestUrl);

    if (!shouldRun) {
        console.log(`BF Script ${BF_VERSION}: Inactive. (Not 'live' and no '?test=bf')`);
        return;
    }
    
    console.log(`BF Script ${BF_VERSION}: Active! Starting injection...`);

    // ==========================================
    // 🎨 STYLES (Immediate Injection)
    // ==========================================
    const injectStyles = () => {
        console.log(`BF Script ${BF_VERSION}: Injecting Styles...`);
        const styles = `
        <style>
            /* 1. ANIMATIONS */
            @keyframes bf-gradient { 0% {background-position: 100% 0;} 100% {background-position: -100% 0;} }
            @keyframes bf-pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
            
            /* Glow Animations (Used for buttons/badges) */
            @keyframes bf-glow { 
                0% { box-shadow: 0 0 8px rgba(212, 33, 44, 0.4); border-color: rgba(212, 33, 44, 0.6); } 
                50% { box-shadow: 0 0 25px rgba(212, 33, 44, 0.7); border-color: rgba(212, 33, 44, 1); } 
                100% { box-shadow: 0 0 8px rgba(212, 33, 44, 0.4); border-color: rgba(212, 33, 44, 0.6); } 
            }
            @keyframes bf-red-glow { 0%, 100% { box-shadow: 0 0 5px ${CONFIG.RED_PRIMARY}; } 50% { box-shadow: 0 0 10px ${CONFIG.RED_PRIMARY}; } }
            @keyframes bf-yellow-glow { 0%, 100% { box-shadow: 0 0 5px ${CONFIG.YELLOW_GLOW}; } 50% { box-shadow: 0 0 10px ${CONFIG.YELLOW_GLOW}; } }
            @keyframes bf-green-glow { 0%, 100% { box-shadow: 0 0 5px ${CONFIG.GREEN_GLOW}; } 50% { box-shadow: 0 0 10px ${CONFIG.GREEN_GLOW}; } }

            :root {
                --bf-red: ${CONFIG.RED_PRIMARY};
                --bf-bg: #050505;
                --bf-card: #161616;
                --bf-yellow-glow: ${CONFIG.YELLOW_GLOW};
                --bf-green-glow: ${CONFIG.GREEN_GLOW};
            }

            /* --- ANNOUNCEMENT BAR STYLES --- */
            #${CONFIG.IDS.ANNOUNCEMENT_BAR} { background-color: var(--bf-red); color: white; font-family: 'Inter', sans-serif; position: relative; z-index: 100; }
            
            .bf-trigger-bar { height: 48px; display: flex; align-items: center; justify-content: center; gap: 12px; cursor: pointer; font-weight: 700; font-size: 0.9rem; text-transform: uppercase; 
                background: linear-gradient(90deg, ${CONFIG.RED_DARK}, var(--bf-red), ${CONFIG.RED_DARK}); 
                background-size: 200% 100%; animation: bf-gradient 3s infinite linear; }
            
            .bf-urgent-badge { background: black; color: var(--bf-red); padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; animation: bf-pulse 1s infinite; }
            
            .bf-expanded-panel { position: absolute; top: 100%; left: 0; width: 100%; background-color: var(--bf-bg); border-bottom: 3px solid var(--bf-red); max-height: 0; opacity: 0; visibility: hidden; transform: translateY(-10px); transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 20px 50px rgba(0,0,0,0.8); overflow: hidden; z-index: 101; }
            
            #${CONFIG.IDS.ANNOUNCEMENT_BAR}:hover .bf-expanded-panel { max-height: 600px; opacity: 1; visibility: visible; transform: translateY(0); }
            
            .bf-wrapper { max-width: 1200px; margin: 0 auto; padding: 30px 20px; display: grid; gap: 30px; grid-template-columns: 1fr; align-items: center; }
            @media (min-width: 900px) { .bf-wrapper { grid-template-columns: 1fr 1.5fr; padding: 40px 30px; } }
            
            .bf-content { text-align: center; display: flex; flex-direction: column; gap: 10px; }
            @media (min-width: 900px) { .bf-content { text-align: left; align-items: flex-start; } }
            
            .bf-status-row { display: flex; gap: 10px; justify-content: center; color: #fbbf24; font-weight: 600; font-size: 0.9rem; }
            @media (min-width: 900px) { .bf-status-row { justify-content: flex-start; } }
            
            .bf-headline { font-size: 3rem; line-height: 0.9; font-weight: 900; text-transform: uppercase; margin: 0; }
            .bf-subheadline { font-size: 1.4rem; color: var(--bf-red); font-weight: 800; }
            
            /* --- PRODUCT CARDS (Shared) --- */
            .bf-products { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
            
            .bf-card { 
                background: var(--bf-card); 
                border: 1px solid #333; 
                border-radius: 12px; 
                padding: 0; /* No padding */
                width: 100%; max-width: 260px; 
                display: flex; flex-direction: column; 
                text-decoration: none; 
                transition: transform 0.2s, border-color 0.2s; 
                position: relative; 
                overflow: hidden; 
            }
            .bf-card:hover { 
                border-color: #666; 
                transform: translateY(-5px); 
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
            }
            
            /* BADGES: Positioned Bottom Right */
            .bf-stock-badge { 
                position: absolute; 
                bottom: 10px; 
                right: 10px; 
                top: auto; left: auto;
                background: #000000; 
                color: white; 
                font-size: 0.75rem; 
                font-weight: 800; 
                padding: 4px 8px; 
                border-radius: 4px; 
                z-index: 10; 
                box-shadow: 0 0 5px var(--bf-yellow-glow); 
                animation: bf-yellow-glow 3s infinite ease-in-out;
                white-space: nowrap; 
                max-width: 90%; overflow: hidden; text-overflow: ellipsis;
            }
            .bf-stock-badge.critical { 
                box-shadow: 0 0 5px var(--bf-red); 
                animation: bf-red-glow 3s infinite ease-in-out; 
            }
            .bf-stock-badge.green-glow { 
                box-shadow: 0 0 5px var(--bf-green-glow); 
                animation: bf-green-glow 3s infinite ease-in-out; 
            }

            /* IMAGE CONTAINER */
            .bf-card-img-container { 
                background: #fff; 
                width: 100%; 
                aspect-ratio: 1 / 1; 
                display: flex; align-items: center; justify-content: center; 
                position: relative; /* Anchor for badge */
                overflow: hidden;
            }
            .bf-card-img { 
                width: 100%; height: 100%; 
                object-fit: cover; /* Fill space */
                padding: 0; 
                box-sizing: border-box; 
                transition: transform 0.3s;
            }
            .bf-card:hover .bf-card-img { transform: scale(1.05); }

            .bf-card-info { padding: 15px; display: flex; flex-direction: column; gap: 6px; flex-grow: 1; }
            .bf-card-title { color: white; font-size: 1rem; font-weight: 600; line-height: 1.3; margin: 0; }
            .bf-price-row { margin-top: auto; display: flex; gap: 10px; align-items: baseline;}
            
            /* WHITE Crossed out price */
            .bf-old-price { 
                color: #ffffff; 
                font-size: 0.9rem; 
                text-decoration: line-through; 
                text-decoration-color: var(--bf-red); 
                text-decoration-thickness: 2px; 
                opacity: 1.0; 
            }
            .bf-new-price { color: var(--bf-red); font-size: 1.2rem; font-weight: 900; }
            
            .bf-card-btn { 
                margin-top: 10px; background: transparent; border: 1px solid #444; color: white; 
                font-size: 0.85rem; text-align: center; padding: 8px 0; border-radius: 6px; 
                font-weight: 600; transition: all 0.2s; text-transform: uppercase; display: block; 
            }
            .bf-card:hover .bf-card-btn { 
                background: var(--bf-red); 
                border-color: var(--bf-red); 
                animation: bf-glow 2s infinite ease-in-out; 
            }
        </style>`;
        document.head.insertAdjacentHTML("beforeend", styles);
    };
    
    // Execute styles IMMEDIATELY
    injectStyles();

    // ==========================================
    // 🏗️ HELPER: Create Card HTML
    // ==========================================
    const createCardHtml = (product) => `
        <a href="${product.link}" class="bf-card">
            <div class="bf-card-img-container">
                ${product.badge ? `<div class="bf-stock-badge ${product.badgeClass || ''}">${product.badge}</div>` : ''}
                <img src="${product.image}" class="bf-card-img" alt="${product.title}">
            </div>
            <div class="bf-card-info">
                <div class="bf-card-title">${product.title}</div>
                <div class="bf-price-row">
                    <span class="bf-old-price">${product.oldPrice}</span>
                    <span class="bf-new-price">${product.newPrice}</span>
                </div>
                <div class="bf-card-btn">Shop Now</div>
            </div>
        </a>
    `;

    // Product Data
    const PRODUCTS = [
        {
            link: "https://brighttools.com.au/products/caravan-cleaning-bundle?_pos=1&_psq=caravan&_ss=e&_v=1.0",
            image: "https://brighttools.com.au/cdn/shop/files/caravan_cleaning_bundle__Silicone.png",
            title: "Caravan Cleaning Bundle",
            oldPrice: "A$234.95", newPrice: "A$169.95",
            badge: "💖 Client’s top choice", badgeClass: "critical"
        },
        {
            link: "https://brighttools.com.au/products/bright-squeegee-pack-squeegee-quick-mop-floor-wipes",
            image: "https://brighttools.com.au/cdn/shop/files/squeegee_floor_wipes_quick_mop_pack.png",
            title: "Bright Squeegee Pack",
            oldPrice: "A$71.90", newPrice: "A$59.95",
            badge: "🔝selling fast today", badgeClass: ""
        },
        {
            link: "https://brighttools.com.au/products/home-cleaning-bundle?srsltid=AfmBOopEQ9UweBxxLLmQhwlzUU_5hAPglv9yznTZJ3D4dt7FhDpvSGAa",
            image: "https://brighttools.com.au/cdn/shop/files/Home_Floor_Cleaning_Bundle_Quick_Mop_Main.jpg?v=1757482350&width=800",
            title: "Home Cleaning Bundle",
            oldPrice: "A$244.00", newPrice: "A$179.95",
            badge: "⭐ Recommended", badgeClass: "green-glow"
        }
    ];

    // ==========================================
    // ⚡ EXECUTION FUNCTIONS
    // ==========================================
    
    const replaceAnnouncementBar = () => {
        const targetElement = document.getElementById(CONFIG.IDS.ANNOUNCEMENT_BAR);
        if (!targetElement) return console.warn(`BF Script ${BF_VERSION}: Announcement Bar Target not found.`);

        // Use all 3 products, or limit to 3 if array gets larger
        const navProductsHtml = PRODUCTS.slice(0, 3).map(createCardHtml).join('');

        const html = `
            <div class="bf-trigger-bar"><span class="bf-urgent-badge">ENDING SOON</span><span>Get Black Friday Deals Now</span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></div>
            <div class="bf-expanded-panel"><div class="bf-wrapper"><div class="bf-content"><div class="bf-status-row"><span>● LIVE NOW</span><span>|</span><span>LAST FEW DAYS</span></div><h2 class="bf-headline">Black Friday</h2><div class="bf-subheadline">UP TO 50% OFF STOREWIDE</div><div style="color: #fff; font-size: 1rem; background: rgba(255,255,255,0.1); padding: 8px 12px; border-radius: 6px; margin-top: 8px; border-left: 4px solid var(--bf-red);">⚠️ <strong>Low Stock Alert:</strong> High demand expected.</div></div><div class="bf-products">${navProductsHtml}</div></div></div>
        `;
        
        const wrapper = document.createElement('aside');
        wrapper.id = CONFIG.IDS.ANNOUNCEMENT_BAR; 
        wrapper.className = targetElement.className; 
        wrapper.innerHTML = html;
        targetElement.replaceWith(wrapper);
        document.documentElement.style.setProperty('--announcement-bar-height', '48px');
        console.log(`BF Script ${BF_VERSION}: ✅ Announcement Bar Replaced`);
    };

    const run = () => {
        replaceAnnouncementBar();
    };

    // Run logic after a slight delay to ensure all theme elements and the main container are available.
    setTimeout(run, 50); 
})();
// 🛑 @raphael.feliz - END BLACK FRIDAY INJECTION SCRIPT 🛑