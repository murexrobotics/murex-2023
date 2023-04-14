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
    form {
      background-color: #F6BD60;
      max-width: 500px;
      margin: 50px auto;
      padding: 30px 20px;
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
      margin-top: 50px;
      margin-bottom: 20px;
    }

    a{
    padding: 15px 32px;
    border: #444;
    text-align: center;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    background-color: #F6BD60;
    }
</style>
<form id="form" action="../update_constants.py" method="POST">
  <div>
    <h3>Thrusters</h3>
    <Textfield status_name="front-right" status={fr}></Textfield>
    <Textfield status_name="front-left" status={fl}></Textfield>
    <Textfield status_name="back-right" status={br}></Textfield>
    <Textfield status_name="back-left" status={bl}></Textfield>
    <Textfield status_name="velocity1" status={v1}></Textfield>
    <Textfield status_name="velocity2" status={v2}></Textfield>
  </div>
  <div>
    <h3>Arm</h3>
    <Textfield status_name="back-left" status={bldc0}></Textfield>
    <Textfield status_name="front-right" status={bldc1}></Textfield>
    <Textfield status_name="front-left" status={bldc2}></Textfield>
    <Textfield status_name="back-right" status={bldc3}></Textfield>
  </div>
  <div>
    <h3>Misc</h3>
    <Textfield status_name="Camera Angle" status={cam_angle}></Textfield>
    <Textfield status_name="Restart Pi?" status={"No"}></Textfield>
    <Textfield status_name="Restart PCA9685?" status={"No"}></Textfield>
    <Textfield status_name="Restart Camera?" status={"No"}></Textfield>
  </div>
    <button type="submit" value="submit">
        UPDATE!
    </button>
  <a href="/" class="button">Exit</a>
</form>