<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';
	/**
	 * @type {any}
	 */
	let tempChart;
	/**
	 * @type {any}
	 */
	export let temperature;
	/**
	 * @type {any}
	 */
	let gasChart;
	/**
	 * @type {any}
	 */
	export let gas;
	/**
	 * @type {any}
	 */
	let humidityChart;
	/**
	 * @type {any}
	 */
	export let humidity;
	/**
	 * @type {any}
	 */
	let pressureChart;
	/**
	 * @type {any}
	 */
	export let pressure;
	/**
	 * @type {any}
	 */
	let altitudeChart;
	/**
	 * @type {any}
	 */
	export let altitude;
	var updateInterval = 200;
	var numberElements = 100;
	var updateCount = [1, 1, 1, 1, 1];
	function addData() {
		if (temperature) {
			tempChart.data.labels = [...tempChart.data.labels, updateCount[0]];
			tempChart.data.datasets[0].data = [...tempChart.data.datasets[0].data, temperature];
			if (updateCount[0] > numberElements) {
				tempChart.data.labels.shift();
				tempChart.data.datasets[0].data.shift();
			}
			updateCount[0]++;
			tempChart.update('none');
		}
		if (gas) {
			gasChart.data.labels = [...gasChart.data.labels, updateCount[1]];
			gasChart.data.datasets[0].data = [...gasChart.data.datasets[0].data, gas];
			if (updateCount[1] > numberElements) {
				gasChart.data.labels.shift();
				gasChart.data.datasets[0].data.shift();
			}
			updateCount[1]++;
			gasChart.update('none');
		}
		if (humidity) {
			humidityChart.data.labels = [...humidityChart.data.labels, updateCount[2]];
			humidityChart.data.datasets[0].data = [...humidityChart.data.datasets[0].data, humidity];
			if (updateCount[2] > numberElements) {
				humidityChart.data.labels.shift();
				humidityChart.data.datasets[0].data.shift();
			}
			updateCount[2]++;
			humidityChart.update('none');
		}
		if (pressure) {
			pressureChart.data.labels = [...pressureChart.data.labels, updateCount[3]];
			pressureChart.data.datasets[0].data = [...pressureChart.data.datasets[0].data, pressure];
			if (updateCount[3] > numberElements) {
				pressureChart.data.labels.shift();
				pressureChart.data.datasets[0].data.shift();
			}
			updateCount[3]++;
			pressureChart.update('none');
		}
		if (altitude) {
			altitudeChart.data.labels = [...altitudeChart.data.labels, updateCount[4]];
			altitudeChart.data.datasets[0].data = [...altitudeChart.data.datasets[0].data, altitude];
			if (updateCount[4] > numberElements) {
				altitudeChart.data.labels.shift();
				altitudeChart.data.datasets[0].data.shift();
			}
			updateCount[4]++;
			altitudeChart.update('none');
		}
	}
	function updateData() {
		addData();
		setTimeout(updateData, updateInterval);
	}
	onMount(async () => {
		tempChart = new Chart(tempChart, {
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
		gasChart = new Chart(gasChart, {
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
		humidityChart = new Chart(humidityChart, {
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
		pressureChart = new Chart(pressureChart, {
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
		altitudeChart = new Chart(altitudeChart, {
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
	<canvas id="tempChart" bind:this={tempChart} />
</div>
<div class="w-1/3">
	<canvas id="gasChart" bind:this={gasChart} />
</div>
<div class="w-1/3">
	<canvas id="humidityChart" bind:this={humidityChart} />
</div>
<div class="w-1/3">
	<canvas id="pressureChart" bind:this={pressureChart} />
</div>
<div class="w-1/3">
	<canvas id="altitudeChart" bind:this={altitudeChart} />
</div>
