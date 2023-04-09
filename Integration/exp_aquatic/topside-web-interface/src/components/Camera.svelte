<script>
    /**
	 * @type {any}
	 */
     export let camera_angle;

     $: x = 150 + 150 * Math.cos(camera_angle * (Math.PI/180))
     $: y = 150 - 150 * Math.sin(camera_angle * (Math.PI/180))

</script>

<p>Degrees: {camera_angle}</p>

<svg class="w-full" viewBox="0 0 300 150" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path id="Circle" d="M 130 150 q 20 -40 40 0" stroke-opacity="0.5" stroke="#EBEBEB" stroke-width="2" fill="none" />
    <line id="Middle_Line" x1="150" y1="0" x2="150" y2="150" stroke="#A54657" stroke-dasharray="4,4" stroke-width="5"/>
    <line id="Bottom_Line" x1="0" y1="150" x2="300" y2="150" stroke="#A54657" stroke-width="5"/>
    <line id="Angle_Line" x1="150" y1="150" x2={x} y2={y} stroke="#F6BD60" stroke-width="5"/>
</svg>