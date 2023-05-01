<script>
    /**
	 * @type {any}
	 */
     export let joystick_left_x;
     /**
	 * @type {any}
	 */
     export let joystick_left_y;
     /**
	 * @type {any}
	 */
      export let joystick_right_x;
      /**
	 * @type {any}
	 */
     export let joystick_right_y;
     /**
	 * @type {any}
	 */
      export let button_a;
     /**
	 * @type {any}
	 */
      export let button_b;
     /**
	 * @type {any}
	 */
      export let button_x;
      /**
	 * @type {any}
	 */
     export let button_y;
     /**
	 * @type {any}
	 */
     export let button_menu;
     /**
	 * @type {any}
	 */
      export let button_xbox;
     /**
	 * @type {any}
	 */
      export let button_view;
     /**
	 * @type {any}
	 */
      export let dpad_up;
    /**
	 * @type {any}
	 */
     export let dpad_down;
     /**
	 * @type {any}
	 */
     export let dpad_left;
     /**
	 * @type {any}
	 */
     export let dpad_right;
     /**
	 * @type {any}
	 */
      export let trigger_right;
      /**
	 * @type {any}
	 */
     export let trigger_left;
     /**
	 * @type {any}
	 */
      export let bumper_right;
     /**
	 * @type {any}
	 */
      export let bumper_left;
      /**
	 * @type {any}
	 */

     function buttonPressed(button){
        if (button == 1){
            return '#F6BD60';
        }
        else {
        return 'none';}
     }

     function changeOpacity(button){
        if (button == 1){
            return '1';
        }
        else {
        return '0.2';}
     }

     $: button_a = buttonPressed(button_a)
     $: button_b = buttonPressed(button_b)
     $: button_x = buttonPressed(button_x)
     $: button_y = buttonPressed(button_y)
     $: button_view = buttonPressed(button_view)
     $: button_menu = buttonPressed(button_menu)
     $: button_xbox = buttonPressed(button_xbox)
     $: dpad_up = changeOpacity(dpad_up)
     $: dpad_down = changeOpacity(dpad_down)
     $: dpad_left = changeOpacity(dpad_left)
     $: dpad_right = changeOpacity(dpad_right)
     $: trigger_right = changeOpacity(trigger_right)
     $: trigger_left = changeOpacity(trigger_left)
     $: bumper_right = changeOpacity(bumper_right)
     $: bumper_left = changeOpacity(bumper_left)
     $: joystick_left_x = joystick_left_x * 27 + 132
     $: joystick_left_y = -joystick_left_y * 27 + 112
     $: joystick_right_x = joystick_right_x * 27 + 340
     $: joystick_right_y = -joystick_right_y * 27 + 196


</script>

<svg class="w-full" viewBox="0 0 536 219" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g id="Group 2" filter="url(#filter0_d_0_1)">
    <path id="bold_left" d="M268 69.5H162L157.417 57L152.833 44.5L147 34.5L133.5 29H108M268 124.5H68M108 29L89.5 47L79.5 66L73.5 86.5L68 104.5V124.5M108 29L82 7.5L65.5 1H49.5L36 7.5L27 19L16.5 34.5L10.5 55L5 73.5M68 124.5L44 114.5L27 102.5L5 73.5M68 124.5L70.5 142L82 161L95 168L108 170.5L141.5 173.5H162L174 177H176M176 177L167 184.5H95L82 173.5L55 164L38.5 151.5L27 137.5L13.5 119L5 96.5V73.5M176 177H246.5L268 179.5" stroke="#F6BD60"/>
    <path id="bold_right" d="M268 69.5H374L378.583 57L383.167 44.5L389 34.5L402.5 29H428M268 124.5H468M428 29L446.5 47L456.5 66L462.5 86.5L468 104.5V124.5M428 29L454 7.5L470.5 1H486.5L500 7.5L509 19L519.5 34.5L525.5 55L531 73.5M468 124.5L492 114.5L509 102.5L531 73.5M468 124.5L465.5 142L454 161L441 168L428 170.5L394.5 173.5H374L362 177M268 179.5L289.5 177H360H406L454 173.5L481 164L497.5 151.5L509 137.5L522.5 119L531 96.5V73.5" stroke="#F6BD60"/>
    <path id="linework" d="M147.5 184V197M147.5 197L158 198L159 207L146 210H133H118L106 207L108 198L116.5 197M147.5 197H116.5M116.5 197V184M191.5 169L155.5 164H116.5L103 162L90 153L85 144L82.5 132L85 102L86.5 87L90 75.5L95.5 59.5L103 49L122 40.5L133.5 43L140.5 49L148.5 62.5L152 78L155.5 100.5V124.5M191.5 169L214 173H325L344 169M191.5 169L203 146.5L226.5 124.5H313L335.5 146.5L344 169M344 169L360 166L377 164.5H414L438 162.5L449 155.5L456.5 140V124.5L454 96L449 76L445 63L438 50.5L426.5 42L412 40.5L400 46.5L390.5 63L386 79L385 96L383.5 110.5V124.5M296.5 176.5L302 184L308.5 186.5L315.5 185.5M315.5 185.5H323M315.5 185.5L321 181.5L323 176.5M323 185.5V197M323 185.5H353M323 197H353M323 197L312 198L310.5 206.5L314 208.5L319.5 209.5H355L360 208.5L363.5 206.5L362.5 198L353 197M353 197V185.5M353 185.5H373.5V182.5M373.5 182.5H395.5V180M373.5 182.5H363.5L361 180L360 176.5M395.5 179.5V180M475 166V173L473 176.5L469.5 179.5H442L438 175L435 179L431.5 182.5H402.5L398.5 180L395.5 177V180M249.5 129H290.5L298 136V146.5H239.5V136L249.5 129Z" stroke="#F6BD60" stroke-opacity="0.6"/>
    <path id="L_Trigger" d="M155.5 124.5H83L86.5 86.5L95.5 59.5L103 49L122 40.5L133.5 43L141 49.5L148.5 62.5L155.5 101V124.5Z" fill="#F6BD60" fill-opacity={trigger_left}/>
    <path id="R_Trigger" d="M454 96L456.5 124.5H383.5V112.5L384.5 100.5L386 79.5L390.5 63.5L400 46.5L412 40.5L426.5 42L438 50.5L445 63.5L454 96Z" fill="#F6BD60" fill-opacity={trigger_right}/>
    <path id="L_Bumper" d="M82.5 132L83.5 124.5H226.5L226 125L203 146.5L202 148.5L191.5 169L155 164H117L103 162L90 153L85 144L83.5 137.5L82.5 132Z" fill="#F6BD60" fill-opacity={bumper_left}/>
    <path id="R_Bumper" d="M335 146L313.5 124.5H456.5V140L449 155.5L438 162.5L413 164.5H377L360 166L344 168.5L335 146Z" fill="#F6BD60" fill-opacity={bumper_right}/>
    </g>
    <defs>
    <filter id="filter0_d_0_1" x="0.5" y="0.5" width="535" height="218" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
    <feFlood flood-opacity="0" result="BackgroundImageFix"/>
    <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
    <feOffset dy="4"/>
    <feGaussianBlur stdDeviation="2"/>
    <feComposite in2="hardAlpha" operator="out"/>
    <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
    <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_0_1"/>
    <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_0_1" result="shape"/>
    </filter>
    </defs>
    </svg>

<svg class="w-full" viewBox="0 0 540 360" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path id="Left" d="M269.5 269H247.5H218L196 272.5L174.5 278.5L150 297L104.5 338.5L88 349L71 357L55 358.5L40 357L21.5 351L7.5 338.5L1 315.5V288L7.5 242.5L14.5 204.5L25.5 165.5L36 126L47.5 91.5L57.5 68.5L71 47.5L81.5 31L95.5 21.5L110.5 14L139 6L151.5 3L164 2L178.5 6L190.5 14H269.5" stroke="#F6BD60" stroke-width="2"/>
    <path id="Right" d="M269.5 269H292.5H322L344 272.5L365.5 278.5L390 297L435.5 338.5L452 349L469 357L485 358.5L500 357L518.5 351L532.5 338.5L539 315.5V288L532.5 242.5L525.5 204.5L514.5 165.5L504 126L492.5 91.5L482.5 68.5L469 47.5L458.5 31L444.5 21.5L429.5 14L401 6L388.5 3L376 2L361.5 6L349.5 14H269.5" stroke="#F6BD60" stroke-width="2"/>
    <path id="R_Linework" d="M269.5 23.5H358.5L369 20L375 18.5H384L394.5 20L418.5 26.5L439.5 34L463 45.5L471 50M269.5 80H301L312 78.5L325.5 75L332.5 69.5L366.5 35.5L377.5 26.5L385 25.5L394.5 26.5L418.5 34L438.5 40.5L463 52.5L480.5 65M269.5 258.5H295L308.5 259L324.5 260L340 261L356.5 264.5L367.5 268L378.5 274L411 302L429 319.5L448 335L466.5 348L481 354.5L493 358M345 23V13.5" stroke="#F6BD60" stroke-opacity="0.6"/>
    <path id="L_Linework" d="M269.5 23.5H180.5L170 20L164 18.5H155L144.5 20L120.5 26.5L99.5 34L76 45.5L69 50M269.5 80H238L227 78.5L213.5 75L206.5 69.5L172.5 35.5L161.5 26.5L154 25.5L144.5 26.5L120.5 34L100.5 40.5L76 52.5L58.5 66M269.5 258.5H244L230.5 259L214.5 260L199 261L182.5 264.5L171.5 268L160.5 274L128 302L110 319.5L91 335L72.5 348L58 354.5L46 358M194 23V13.5" stroke="#F6BD60" stroke-opacity="0.6"/>
    <circle id="L_Outer" cx="132" cy="112" r="45" stroke="#F6BD60" stroke-width="2"/>
    <circle id="L_Inner" cx="132" cy="112" r="35" fill="#F6BD60" opacity="0.2"/>
    <circle id="D_Outer" cx="200" cy="204" r="45" stroke="#F6BD60" stroke-width="2"/>
    <circle id="R_Outer" cx="340" cy="196" r="45" stroke="#F6BD60" stroke-width="2"/>
    <circle id="R_Inner" cx="340" cy="196" r="35" fill="#F6BD60" opacity="0.2"/>
    <circle id="L_Joystick" cx={joystick_left_x} cy={joystick_left_y} r="27" fill="#F6BD60"/>
    <circle id="R_Joystick" cx={joystick_right_x} cy={joystick_right_y} r="27" fill="#F6BD60"/>
    <path id="D_Up" d="M186 161H214V218H186V161Z" fill="#F6BD60" opacity = {dpad_up}/>
    <path id="D_Right" d="M186 218V190H243V218H186Z" fill="#F6BD60" opacity = {dpad_right}/>
    <path id="D_Left" d="M157 218V190H214V218H157Z" fill="#F6BD60" opacity = {dpad_left}/>
    <path id="D_Down" d="M186 190H214V247H186V190Z" fill="#F6BD60" opacity = {dpad_down}/>
    <path id="Y" d="M439 73.5C439 85.3741 429.374 95 417.5 95C405.626 95 396 85.3741 396 73.5C396 61.6259 405.626 52 417.5 52C429.374 52 439 61.6259 439 73.5Z" stroke="#F6BD60" fill = {button_y} stroke-width="2"/>
    <path id="X" d="M399 112.5C399 123.822 389.822 133 378.5 133C367.178 133 358 123.822 358 112.5C358 101.178 367.178 92 378.5 92C389.822 92 399 101.178 399 112.5Z" stroke="#F6BD60" fill = {button_x} stroke-width="2"/>
    <path id="B" d="M476 112.5C476 123.822 466.822 133 455.5 133C444.178 133 435 123.822 435 112.5C435 101.178 444.178 92 455.5 92C466.822 92 476 101.178 476 112.5Z" stroke="#F6BD60" fill = {button_b} stroke-width="2"/>
    <path id="A" d="M438 150.5C438 161.822 428.822 171 417.5 171C406.178 171 397 161.822 397 150.5C397 139.178 406.178 130 417.5 130C428.822 130 438 139.178 438 150.5Z" stroke="#F6BD60" fill = {button_a} stroke-width="2"/>
    <circle id="Menu" cx="310" cy="112" r="16" fill={button_menu} stroke="#F6BD60" stroke-width="2"/>
    <circle id="View" cx="230" cy="112" r="16" fill={button_view} stroke="#F6BD60" stroke-width="2"/>
    <circle id="Xbox" cx="269.5" cy="53.5" r="21.5" fill={button_xbox} stroke="#F6BD60" stroke-width="4"/>
    </svg>