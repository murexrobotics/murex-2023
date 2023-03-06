<script>
	import { parse } from 'postcss';
    import { onMount } from 'svelte';
    import "../app.css";
    import Sensors from '../components/Sensors.svelte';
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
    let temperature, gas, humidity, pressure, altitude, bme680;
    onMount(() => {
		websocket = new WebSocket("ws://localhost:5678/");
		websocket.onmessage = ({
			data
		}) => {
            inputFromWebsocket = String(data);
            parsedInput = JSON.parse(inputFromWebsocket)
            websocketTime = parsedInput.time
            temperature = parsedInput.bme680.temperature
            gas = parsedInput.bme680.gas
            humidity = parsedInput.bme680.humidity
            pressure = parsedInput.bme680.pressure
            altitude = parsedInput.bme680.altitude
            bme680 = parsedInput.bme680
		};
    })
    $: {
        console.log(parsedInput)
    }
</script>

<h1 class="whitespace-pre">
    {inputFromWebsocket}
</h1>

<Sensors temperature={temperature} gas={gas} humidity={humidity} pressure={pressure} altitude={altitude}></Sensors>