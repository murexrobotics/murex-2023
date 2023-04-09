<script>
    /**
	 * @type {any}
	 */
     export let websocketTime;
</script>

<nav class="flex items-center justify-between flex-wrap p-6">
    <a href="#responsive-header" class="flex justify-between rounded-lg bg-light-blue text-white hover:text-red">
      <svg class ="h-12 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" >
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      
        <h2 class="font-bold text-white py-3">Time: {websocketTime}</h2>
    </a>
  </nav>
