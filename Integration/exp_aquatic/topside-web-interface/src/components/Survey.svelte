<script>
    // @ts-ignore
    import { parse } from 'postcss';
    import { onMount } from 'svelte';
    import "../app.css";
    // @ts-ignore
    import Textfield from './Textfield.svelte';
    /**
   * @type {any}
   */
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
<form class = "relative w-screen h-screen" id="form" action="../src/update_constants.py" enctype="multipart/form-data" method="POST">
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
    <Textfield status_name="Joystick_maximum" status={0.2}></Textfield>
    <Textfield status_name="PCA_Frequency" status={50}></Textfield>
    <Textfield status_name="Neopixel_brightness" status={0.2}></Textfield>
  </div>
  <div id="field" class = "absolute w-1/4 p-3 rounded-lg bg-white bg-opacity-5" style="top:10%;left:37%">
    <h3>Reboot</h3>
    <Textfield status_name="Restart_Pi?" status={"No"}></Textfield>
    <Textfield status_name="Restart_PCA9685?" status={"No"}></Textfield>
    <Textfield status_name="Restart_Camera?" status={"No"}></Textfield>
  </div>
  <div id="field" class = "absolute w-1/6 p-3 rounded-lg bg-white bg-opacity-5" style="bottom:10%;left:41%">
    <button class="button" type="submit" value="submit">
      UPDATE!
    </button>
    <a href="/" class="button">Exit</a>
  </div>
</form>