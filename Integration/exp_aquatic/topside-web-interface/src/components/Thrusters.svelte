<script>
    /**
	 * @type {any}
	 */
     export let fr;
     /**
	 * @type {any}
	 */
      export let fl;
     /**
	 * @type {any}
	 */
      export let br;
     /**
	 * @type {any}
	 */
      export let bl;
     /**
	 * @type {any}
	 */
      export let v1;
      /**
	 * @type {any}
	 */
     export let v2;

     function small_thruster(power){
        return power * 375;
     }

     function large_thruster(power){
        return power * 1000;
     }

     function opacity(power)
     {
        if (power == 0)
        { return 0; }
        return 1;
     }

     $: fr_x = small_thruster(fr) + 2840
     $: fr_y = small_thruster(fr) + 526
     $: fr_opacity = opacity(fr)
     $: fl_x = -small_thruster(fl) + 1108
     $: fl_y = small_thruster(fl) + 526
     $: fl_opacity = opacity(fl)
     $: br_x = -small_thruster(br) + 2840
     $: br_y = small_thruster(br) + 2008
     $: br_opacity = opacity(br)
     $: bl_x = small_thruster(bl) + 1134
     $: bl_y = small_thruster(bl) + 2008
     $: bl_opacity = opacity(bl)
     $: v1 = large_thruster(v1) + 1266.5
     $: v1_opacity = opacity(v2)
     $: v2 = large_thruster(v2) + 1266.5
     $: v2_opacity = opacity(v2)
</script>

<svg class="w-full" viewBox="0 0 3943 2518" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path id="Outline" d="M2917 2507.5H1026C862.884 2471.31 776.113 2439.28 627 2368L333.5 2118L112 1742.5C57.1425 1576.77 11 1271 11 1271C11 1271 54.4462 978.809 112 809L222.75 623.75L333.5 438.5L480.25 316L627 193.5L1026 10.5H2917L3316 193.5L3462.75 316L3609.5 438.5L3720.25 623.75L3831 809C3888.55 978.809 3932 1271 3932 1271C3932 1271 3885.86 1576.77 3831 1742.5L3609.5 2118L3316 2368C3166.89 2439.28 3080.12 2471.31 2917 2507.5Z" stroke="#F6BD60" stroke-width="20"/>
    <g id="Small_Hole" filter="url(#filter0_i_0_1)">
    <path d="M1782.5 515C1782.5 600.052 1713.55 669 1628.5 669C1543.45 669 1474.5 600.052 1474.5 515C1474.5 429.948 1543.45 361 1628.5 361C1713.55 361 1782.5 429.948 1782.5 515ZM2395.5 515C2395.5 600.052 2326.55 669 2241.5 669C2156.45 669 2087.5 600.052 2087.5 515C2087.5 429.948 2156.45 361 2241.5 361C2326.55 361 2395.5 429.948 2395.5 515ZM1782.5 2019.5C1782.5 2104.55 1713.55 2173.5 1628.5 2173.5C1543.45 2173.5 1474.5 2104.55 1474.5 2019.5C1474.5 1934.45 1543.45 1865.5 1628.5 1865.5C1713.55 1865.5 1782.5 1934.45 1782.5 2019.5ZM2395.5 2019.5C2395.5 2104.55 2326.55 2173.5 2241.5 2173.5C2156.45 2173.5 2087.5 2104.55 2087.5 2019.5C2087.5 1934.45 2156.45 1865.5 2241.5 1865.5C2326.55 1865.5 2395.5 1934.45 2395.5 2019.5Z" stroke="#F6BD60" stroke-opacity="0.5" stroke-width="10"/>
    </g>
    <circle id="fr_base" cx="2840" cy="526" r="78" fill="#F6BD60" fill-opacity="0.2"/>
    <circle id="fr_circle" cx="2840" cy="526" r="78" fill="#F6BD60" opacity={fr_opacity}/>
    <line id="fr_line" x1="2840" y1="526" x2={fr_x} y2={fr_y} stroke="#F6BD60" stroke-opacity={fr_opacity} stroke-width="50" stroke-linecap="round"/>
    <circle id="fl_base" cx="1108" cy="526" r="78" fill="#F6BD60" fill-opacity="0.2"/>
    <circle id="fl_circle" cx="1108" cy="526" r="78" fill="#F6BD60" opacity={fl_opacity}/>
    <line id="fl_line" x1="1108" y1="526" x2={fl_x} y2={fl_y} stroke="#F6BD60" stroke-opacity={fl_opacity} stroke-width="50" stroke-linecap="round"/>
    <circle id="br_base" cx="2840" cy="2008" r="78" fill="#F6BD60" fill-opacity="0.2"/>
    <circle id="br_circle" cx="2840" cy="2008" r="78" fill="#F6BD60" opacity={br_opacity}/>
    <line id="br_line" x1="2840" y1="2008" x2={br_x} y2={br_y} stroke="#F6BD60" stroke-opacity={br_opacity} stroke-width="50" stroke-linecap="round"/>
    <circle id="bl_base" cx="1134" cy="2008" r="78" fill="#F6BD60" fill-opacity="0.2"/>
    <circle id="bl_circle" cx="1134" cy="2008" r="78" fill="#F6BD60" opacity={bl_opacity}/>
    <line id="bl_line" x1="1134" y1="2008" x2={bl_x} y2={bl_y} stroke="#F6BD60" stroke-opacity={bl_opacity} stroke-width="50" stroke-linecap="round"/>
    <circle id="v1_base" cx="636.5" cy="1266.5" r="296.5" fill="#F6BD60" fill-opacity="0.2"/>
    <circle id="v1_circle" cx="636.5" cy="1266.5" r="296.5" fill="#F6BD60" opacity={v1_opacity}/>
    <line id="vl_line" x1="636.5" y1="1266.5" x2=636.5 y2={v1} stroke="#F6BD60" stroke-opacity={v1_opacity} stroke-width="50" stroke-linecap="round"/>
    <circle id="v2_base" cx="3233.5" cy="1267.5" r="296.5" fill="#F6BD60" fill-opacity="0.2"/>
    <circle id="v2_circle" cx="3233.5" cy="1266.5" r="296.5" fill="#F6BD60" opacity={v2_opacity}/>
    <line id="v2_line" x1="3233.5" y1="1266.5" x2=3233.5 y2={v2} stroke="#F6BD60" stroke-opacity={v2_opacity} stroke-width="50" stroke-linecap="round"/>
    <defs>
    <filter id="filter0_i_0_1" x="1469.5" y="356" width="931" height="1826.5" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
    <feFlood flood-opacity="0" result="BackgroundImageFix"/>
    <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
    <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
    <feOffset dy="4"/>
    <feGaussianBlur stdDeviation="2"/>
    <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
    <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
    <feBlend mode="normal" in2="shape" result="effect1_innerShadow_0_1"/>
    </filter>
    </defs>
    </svg>