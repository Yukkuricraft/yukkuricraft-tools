<template>
	<normal-page parallax-class="parallax-download">
		<template v-slot:parallax>
			<h1>Past Survival downloads</h1>
			<p>Download the maps of past survival worlds</p>
		</template>

		<div class="alert alert-warning mt-3" role="alert" style="font-size: 85%">
			<h2 class="alert-heading h5">Compatability and old versions</h2>
			<p class="mb-2">
				These maps have never been taken to a newer Minecraft version than what we list here. It might work just
				fine, it might go absolutely terrible. For the best experience, play the map on the version it was intended
				for.
			</p>
		</div>

		<ul>
			<li><a href="https://mega.nz/file/4kdnXZxB#m3v01SsD_ZKmjRdQBxnCdHBnvaG8wzcXKZuciJ1z7hw">Survival 1: 1.6 (2012-2014)</a></li>
			<li><a href="https://mega.nz/#!QgtwhbwJ!5nxZBAWxpCAjk4el5nuVDylCs1RqWzQT3WFtQj8%20mIOo">Survival 2 (Neo Survival): 1.8 (2014-2016)</a></li>
			<li><a href="https://mega.nz/#F!kpd1hAzb!9h3daouqqfFpgF1tpx1F5A">Survival 3 (Nova Survival): 1.12 (2016-2019)</a></li>
		</ul>

		<p>
			<strong>CHROME USERS</strong> - Mega is known to have issues downloading on Chrome. If you are using Chrome and
			having difficulty downloading, please temporarily use Firefox or some other browser of your choice to download
			from that link.
		</p>
	</normal-page>
</template>

<script>
	import NormalPage from "../../layout/NormalPage";
	export default {
		components: {NormalPage}
	}
</script>