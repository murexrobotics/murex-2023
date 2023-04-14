<script>
/**
 * @type {any}
 */
   export let status_name;
   /**
 * @type {any}
 */
    export let status;
</script>

<style>

  .form-control {
      text-align: left;
      margin-bottom: 25px;
  }

  /* Styling form-control Label */
  .form-control label {
      display: block;
      margin-bottom: 10px;
  }

  .form-control input{
      border: 1px solid #444;
      border-radius: 2px;
      font-family: inherit;
      padding: 10px;
      display: block;
      width: 95%;
  }
</style>

<div class="form-control">
  <label for="name" id="label-name">
      {status_name}
  </label>
  <input type="text" id={status_name} value={status}/>
</div>