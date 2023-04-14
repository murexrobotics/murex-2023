<script>
	import { parse } from 'postcss';
    import { onMount } from 'svelte';
    import "../app.css";
    import Sensors from '../components/Sensors.svelte';
    import Chart from '../components/Chart.svelte';
    import Thrusters from '../components/Thrusters.svelte';
    import Joystick from '../components/Joystick.svelte';
	import Navbar from '../components/Navbar.svelte';
	import Camera from '../components/Camera.svelte';
    import Button from '../components/Button.svelte';
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
    let camera_angle, fr, fl, br, bl, v1, v2, temperature, gas, humidity, pressure, altitude, bme680, joystick_left_x, joystick_left_y, joystick_right_x, joystick_right_y, button_y, button_x, button_b, button_a, button_menu, button_view, button_xbox, trigger_right, trigger_left, bumper_right, bumper_left, dpad_up, dpad_down, dpad_left, dpad_right;
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
            temperature = parsedInput.bme680.temperature
            gas = parsedInput.bme680.gas
            humidity = parsedInput.bme680.humidity
            pressure = parsedInput.bme680.pressure
            altitude = parsedInput.bme680.altitude
            bme680 = parsedInput.bme680
            joystick_left_x = parsedInput.joystick.joystick_left_x
            joystick_left_y = parsedInput.joystick.joystick_left_y
            joystick_right_x = parsedInput.joystick.joystick_right_x
            joystick_right_y = parsedInput.joystick.joystick_right_y
            button_y = parsedInput.joystick.button_y
            button_x = parsedInput.joystick.button_x
            button_b = parsedInput.joystick.button_b
            button_a = parsedInput.joystick.button_a
            button_menu = parsedInput.joystick.button_menu
            button_view = parsedInput.joystick.button_view
            button_xbox = parsedInput.joystick.button_xbox
            trigger_right = parsedInput.joystick.trigger_right
            trigger_left = parsedInput.joystick.trigger_left
            bumper_right = parsedInput.joystick.bumper_right
            bumper_left = parsedInput.joystick.bumper_left
            dpad_up = parsedInput.joystick.dpad_up
            dpad_down = parsedInput.joystick.dpad_down
            dpad_left = parsedInput.joystick.dpad_left
            dpad_right = parsedInput.joystick.dpad_right
		};
    })
    $: {
        console.log(parsedInput)
    }
</script>

<!-- <h1 class="whitespace-pre">
    {inputFromWebsocket}
</h1> -->

<body class = "h-screen w-screen bg-no-repeat bg-cover bg-center bg-murex-gif" >
    <div class = "relative w-screen h-4/5">
        <div class = "absolute w-1/3 top-16 left-16 p-5 rounded-lg bg-white bg-opacity-5">
            <div></div>
            <Joystick joystick_left_x={joystick_left_x} joystick_left_y={joystick_left_y} joystick_right_x={joystick_right_x} joystick_right_y={joystick_right_y} button_y={button_y}  button_x={button_x}  button_b={button_b}  button_a={button_a}  button_menu={button_menu} button_view={button_view} button_xbox={button_xbox} trigger_right={trigger_right}  trigger_left={trigger_left}  bumper_right={bumper_right}  bumper_left={bumper_left}  dpad_up={dpad_up} dpad_down={dpad_down} dpad_left={dpad_left} dpad_right={dpad_right}> trigger_right={trigger_right} trigger_left={trigger_left} bumper_right={bumper_right} bumper_left={bumper_left}</Joystick> 
        </div>
        <div class = "absolute w-1/3 top-16 left-16 p-5 rounded-lg bg-white bg-opacity-5">
            <div></div>
            <Joystick joystick_left_x={joystick_left_x} joystick_left_y={joystick_left_y} joystick_right_x={joystick_right_x} joystick_right_y={joystick_right_y} button_y={button_y}  button_x={button_x}  button_b={button_b}  button_a={button_a}  button_menu={button_menu} button_view={button_view} button_xbox={button_xbox} trigger_right={trigger_right}  trigger_left={trigger_left}  bumper_right={bumper_right}  bumper_left={bumper_left}  dpad_up={dpad_up} dpad_down={dpad_down} dpad_left={dpad_left} dpad_right={dpad_right}> trigger_right={trigger_right} trigger_left={trigger_left} bumper_right={bumper_right} bumper_left={bumper_left}</Joystick> 
        </div>
        <div class = "absolute w-1/3 top-4 right-16 p-3 rounded-lg bg-white bg-opacity-5">
            <Thrusters fr={fr} fl={fl} br={br} bl={bl} v1={v1}  v2={v2}> </Thrusters> 
        </div>
        <div class = "absolute w-1/3 bottom-8 right-16 p-3 rounded-lg bg-white bg-opacity-5">
            <Camera camera_angle={camera_angle}></Camera>
        </div>
        <div class = "absolute p-3 rounded-lg bg-white bg-opacity-5" style="top:10%;left:44%">
            <Button fr={fr} fl={fl} br={br} bl={bl} v1={v1}  v2={v2}> </Button> 
        </div>
    </div>

    <div class = "">
        <div class= "absolute inset-x-0 bottom-4 h-1/5 left-2 right-2">
            <Chart temperature={temperature} gas={gas} humidity={humidity} pressure={pressure} altitude={altitude}></Chart>
        </div>
    </div>


</body>