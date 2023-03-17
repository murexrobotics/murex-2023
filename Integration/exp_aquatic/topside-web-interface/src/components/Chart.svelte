<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	/**
	 * @type {any}
	 */
	let charts = [];
	/**
	 * @type {any}
	 */
	export let temperature;
	/**
	 * @type {any}
	 */
	export let gas;
	/**
	 * @type {any}
	 */
	export let humidity;
	/**
	 * @type {any}
	 */
	export let pressure;
	/**
	 * @type {any}
	 */
	export let altitude;
	var updateInterval = 200;
	var numberElements = 100;
	var updateCount = [1, 1, 1, 1, 1];
	function addData() {
		var vals = [temperature, gas, humidity, pressure, altitude];
		for(var i = 0; i < 5; i++) {
			if(vals[i]) {
				charts[i].data.labels = [...charts[i].data.labels, updateCount[i]];
				charts[i].data.datasets[0].data = [...charts[i].data.datasets[0].data, vals[i]];
				if (updateCount[i] > numberElements) {
					charts[i].data.labels.shift();
					charts[i].data.datasets[0].data.shift();
				}
				updateCount[i]++;
				charts[i].update('none');
			}
		}
	}
	function updateData() {
		addData();
		setTimeout(updateData, updateInterval);
	}
	onMount(async () => {
		charts[0] = new Chart(charts[0], {
			type: 'line',
			data: {
				labels: [0],
				datasets: [
					{
						label: 'Temperature',
						data: [temperature],
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
		charts[1] = new Chart(charts[1], {
			type: 'line',
			data: {
				labels: [0],
				datasets: [
					{
						label: 'Gas',
						data: [gas],
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
		charts[2] = new Chart(charts[2], {
			type: 'line',
			data: {
				labels: [0],
				datasets: [
					{
						label: 'Humidity',
						data: [humidity],
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
		charts[3] = new Chart(charts[3], {
			type: 'line',
			data: {
				labels: [0],
				datasets: [
					{
						label: 'Pressure',
						data: [pressure],
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
		charts[4] = new Chart(charts[4], {
			type: 'line',
			data: {
				labels: [0],
				datasets: [
					{
						label: 'Altitude',
						data: [altitude],
						borderWidth: 1
					}
				]
			},
			options: {
				scales: {
					y: {
						beginAtZero: true
					}
				}
			}
		});
		updateData();
	});
</script>

<div class="w-1/3">
	<canvas id="tempChart" bind:this={charts[0]} />
</div>
<div class="w-1/3">
	<canvas id="gasChart" bind:this={charts[1]} />
</div>
<div class="w-1/3">
	<canvas id="humidityChart" bind:this={charts[2]} />
</div>
<div class="w-1/3">
	<canvas id="pressureChart" bind:this={charts[3]} />
</div>
<div class="w-1/3">
	<canvas id="altitudeChart" bind:this={charts[4]} />
</div>
