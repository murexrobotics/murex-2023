<script>
	// @ts-ignore
	import { parse } from 'postcss';
    import { onMount } from 'svelte';
    import "../../app.css";
    // @ts-ignore
    import Survey from '../../components/Survey.svelte';
    let name = 'byran';
    let websocket;
    /**
	 * @type {any}
	 */
    let websocketTime;
    /**
	 * @type {any}
	 */
    let parsedInput;
    /**
	 * @type {any}
	 */
    let inputFromWebsocket;
    /**
	 * @type {any}
	 */
    let camera_angle, fr, fl, br, bl, v1, v2, bldc0, bldc1, bldc2, bldc3, bme680;
    onMount(() => {
		websocket = new WebSocket("ws://localhost:5678/");
		websocket.onmessage = ({
			data
		}) => {
            inputFromWebsocket = String(data);
            parsedInput = JSON.parse(inputFromWebsocket)
            websocketTime = parsedInput.time
            camera_angle = parsedInput.camera_angle
            fr = parsedInput.thruster.fr
            fl = parsedInput.thruster.fl
            br = parsedInput.thruster.br
            bl = parsedInput.thruster.fl
            v1 = parsedInput.thruster.v1
            v2 = parsedInput.thruster.v2
            bme680 = parsedInput.bme680
            bldc0 = parsedInput.arm.bldc0
            bldc1 = parsedInput.arm.bldc1
            bldc2 = parsedInput.arm.bldc2
            bldc3 = parsedInput.arm.bldc3
		};
    })
   // @ts-ignore
     $: {
        console.log(parsedInput)
    }
</script>

<!-- <h1 class="whitespace-pre">
    {inputFromWebsocket}
</h1> -->

<body class = "h-screen w-screen bg-no-repeat bg-cover bg-center" >
    <Survey fr={fr}, fl={fl}, br={br}, bl={bl}, v1={v1}, v2={v2}, bldc0={bldc0}, bldc1={bldc1}, bldc2={bldc2}, bldc3={bldc3}></Survey>
</body>