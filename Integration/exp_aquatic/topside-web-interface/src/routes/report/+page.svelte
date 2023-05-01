<script>
    import { parse } from 'postcss';
    import { onMount } from 'svelte';
    import "../../app.css";
    import Textfield from '../../components/Textfield.svelte';
	  import { update_await_block_branch } from 'svelte/internal';

    const IP = "localhost";
    const PORT = 6789;
  
    const status_names = [
    'SEA_LEVEL_PRESSURE',
    'TEMPERATURE_OFFSET',
    'Camera_angle_speed',
    'Joystick_maximum',
    'PCA_Frequency',
    'Telemetry_Period',
    'MIN_PULSE_WIDTH',
    'MAX_PULSE_WIDTH',
    'STOP_DUTY_CYCLE',
    'MAX_DUTY_CYCLE',
    'MIN_DUTY_CYCLE',
    'THRUSTER_INIT_TIME',
    'Restart_Pi?',
    'Restart_PCA9685?',
    'Restart_Camera?'];

    var values = [1013.25,-5,15,0.4,50,0.05,1100,1900,5232,6880,3600,7,0,0,0];


    let socket;

    function update(){
      // Backup signals through websocket
      socket = new WebSocket("ws://localhost:6789/");
      socket.onopen = () => {
          console.log('WebSocket connection established');
      };
      socket.onopen = () => {
          console.log('WebSocket connection established');
      };
      socket.onmessage = (event) => {
          console.log(`Received message: ${event.data}`);
      };
      socket.onerror = (error) => {
          console.error(`WebSocket error: ${error}`);
      };
      socket.onclose = () => {
          console.log('WebSocket connection closed');
      };
      for(var i=0; i<status_names.length; i++){
          var change = document.getElementById(status_names[i]).value;
          values[i] = document.getElementById(status_names[i]).value;
          
          var command = status_names[i] + " : " + change;
          console.log(command);
          socket.send(JSON.stringify("Telemetry Payload Sent" + command));
      }
      socket.close();
    };
  </script>

  <style>
      #field{
        background-color: #F6BD60;
        box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
        color: #444;
      }
      
      .button {
        background-color: #db5d44;
        border-radius: 10px;
        font-family: inherit;
        font-size: 21px;
        display: block;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 20px;
      }
  
      a{
        padding: 15px 32px;
        text-align: center;
        display: inline-block;
        font-size: 30px;
        margin: 4px 2px;
        background-color: #F6BD60;
      }
  
      h3{
        font-size: 30px;
        font-weight: bold;
      }
  </style>
  <body class = "h-screen w-screen bg-no-repeat bg-cover bg-center" >
    <form class = "relative w-screen h-screen" id="form" action="../" enctype="multipart/form-data">
      <div id="field" class = "absolute w-1/4 left-8 top-8 p-3 rounded-lg bg-white bg-opacity-5">
        <h3>Thrusters</h3>
        <Textfield status_name="MIN_PULSE_WIDTH" status={1100}></Textfield>
        <Textfield status_name="MAX_PULSE_WIDTH" status={1900}></Textfield>
        <Textfield status_name="STOP_DUTY_CYCLE" status={5232}></Textfield>
        <Textfield status_name="MAX_DUTY_CYCLE" status={6880}></Textfield>
        <Textfield status_name="MIN_DUTY_CYCLE" status={3600}></Textfield>
        <Textfield status_name="THRUSTER_INIT_TIME" status={7}></Textfield>
      </div>
      <div id="field" class = "absolute w-1/4 right-8 top-8 p-3 rounded-lg bg-white bg-opacity-5">
        <h3>Misc.</h3>
        <Textfield status_name="SEA_LEVEL_PRESSURE" status={1013.25}></Textfield>
        <Textfield status_name="TEMPERATURE_OFFSET" status={-5}></Textfield>
        <Textfield status_name="Camera_angle_speed" status={15}></Textfield>
        <Textfield status_name="Joystick_maximum" status={0.4}></Textfield>
        <Textfield status_name="PCA_Frequency" status={50}></Textfield>
        <Textfield status_name="Telemetry_Period" status={0.05}></Textfield>
      </div>
      <div id="field" class = "absolute w-1/4 p-3 rounded-lg bg-white bg-opacity-5" style="top:10%;left:37%">
        <h3>Reboot</h3>
        <Textfield status_name="Restart_Pi?" status={"No"}></Textfield>
        <Textfield status_name="Restart_PCA9685?" status={"No"}></Textfield>
        <Textfield status_name="Restart_Camera?" status={"No"}></Textfield>
      </div>
      <div id="field" class = "absolute w-1/6 p-3 rounded-lg bg-white bg-opacity-5" style="bottom:10%;left:41%">
        <button class="button" on:click={update} >UPDATE!</button>
        <a href="/" class="button">Exit</a>
      </div>
    </form>
  </body>