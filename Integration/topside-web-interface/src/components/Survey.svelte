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
   export let fr,fl,br,bl,v1,v2,bldc0,bldc1,bldc2,bldc3,cam_angle;
</script>
<style>
    #field{
      background-color: #F6BD60;
      box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
      color: #444;
    }
    
    button {
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
      font-size: 35px;
      font-weight: bold;
    }
</style>
<form class = "relative w-screen h-screen" id="form" action="../update_constants.py" method="POST">
  <div id="field" class = "absolute w-1/3 left-8 top-8 p-3 rounded-lg bg-white bg-opacity-5">
    <h3>Thrusters</h3>
    <Textfield status_name="front-right" status={fr}></Textfield>
    <Textfield status_name="front-left" status={fl}></Textfield>
    <Textfield status_name="back-right" status={br}></Textfield>
    <Textfield status_name="back-left" status={bl}></Textfield>
  </div>
  <div id="field" class = "absolute w-1/3 right-8 top-8 p-3 rounded-lg bg-white bg-opacity-5">
    <h3>Arm</h3>
    <Textfield status_name="BLDC0" status={bldc0}></Textfield>
    <Textfield status_name="BLDC1" status={bldc1}></Textfield>
    <Textfield status_name="BLDC2" status={bldc2}></Textfield>
    <Textfield status_name="BLDC3" status={bldc3}></Textfield>
  </div>
  <div id="field" class = "absolute w-1/3 left-8 bottom-8 p-3 rounded-lg bg-white bg-opacity-5">
    <h3>Reboot</h3>
    <Textfield status_name="Restart Pi?" status={"No"}></Textfield>
    <Textfield status_name="Restart PCA9685?" status={"No"}></Textfield>
    <Textfield status_name="Restart Camera?" status={"No"}></Textfield>
  </div>
  <div id="field" class = "absolute w-1/3 right-8 bottom-8 p-3 rounded-lg bg-white bg-opacity-5">
    <button type="submit" value="submit">
      UPDATE!
    </button>
    <a href="/" class="button">Exit</a>
  </div>
</form>