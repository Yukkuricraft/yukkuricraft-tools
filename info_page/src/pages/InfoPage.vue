<template>
	<normal-page parallax-class="parallax-info">
		<template v-slot:parallax>
			<h1>Yukkuricraft Info</h1>
			<p>A collection of information so you don't have to go looking for it elsewhere.</p>
			<p class="lead">Server IP: mc.yukkuricraft.net</p>

			<router-link :to="{'name': 'download_genso'}" v-slot="{ href, navigate }">
				<a class="btn btn-primary" :href="href" @click="navigate">Map download</a>
			</router-link>
			<router-link :to="{'name': 'download_survival'}" v-slot="{ href, navigate }">
				<a class="btn btn-primary" :href="href" @click="navigate">Survival download</a>
			</router-link>
		</template>

		<iframe class="mt-5" width="1120" height="630" src="https://www.youtube-nocookie.com/embed/L6mD2zj8CGs"
				frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
				allowfullscreen></iframe>

		<h2 id="subdomains" class="scrolltarget">Our Subdomains and Pages</h2>
		<h3>General</h3>
		<ul>
			<li><a href="https://yukkuricraft.net" target="_blank">https://yukkuricraft.net</a> - Our main forum and
				page!
			</li>
			<li><a href="http://info.yukkuricraft.net" target="_blank">http://info.yukkuricraft.net</a> - You're
				looking at
				it right now!
			</li>
			<li>mc.yukkuricraft.net - Join this IP to play on our server!</li>
			<li><a href="http://mc.yukkuricraft.net:18123" target="_blank">http://mc.yukkuricraft.net:18123</a> -
				Our
				dynmap!
			</li>
			<li><a href="http://bugs.yukkuricraft.net" target="_blank">http://bugs.yukkuricraft.net</a> - This will
				take you
				to a page where you can submit a bug report for anything that needs to be fixed! No login required!
			</li>
			<li><a href="http://discord.yukkuricraft.net/" target="_blank">http://discord.yukkuricraft.net/</a> -
				Our
				Discord server
			</li>
		</ul>

		<h3>Social media</h3>
		<ul>
			<li><a href="http://www.facebook.com/yukkuricraft" target="_blank">http://www.facebook.com/yukkuricraft</a>
				-
				Facebook Page
			</li>
			<li><a href="http://www.facebook.com/groups/yukkuricraft" target="_blank">http://www.facebook.com/groups/yukkuricraft</a>
				- Facebook Group
			</li>
			<li><a href="http://steamcommunity.com/groups/yukkuricraft" target="_blank">http://steamcommunity.com/groups/yukkuricraft</a>
				- Steam Group
			</li>
		</ul>

		<h2 id="contact" class="scrolltarget">Contact Us</h2>
		<p>Honestly, there isn't much to say. This is Remi_Scarlet's contact information. Contact me with your
			preferred
			method.
		</p>
		<ol>
			<li><strong>Email: </strong>scarletjaeger (@) gmail.com</li>
			<li><strong>Discord: </strong>Remi#5619</li>
			<li><strong>Steam: </strong>Mr. Bromilia Amatsukaze Scarlet</li>
		</ol>

		<p>Also consider joining our <a href="http://steamcommunity.com/groups/yukkuricraft">Steam Group</a> and
			liking our
			<a href="https://facebook.com/yukkuricraft">Facebook Page</a>!
		</p>
		<br/>
	</normal-page>
</template>

<script>
	import ParallaxImage from "../components/ParallaxImage";
	import InfoFooter from "../components/InfoFooter";
	import NormalPage from "../layout/NormalPage";

	export default {
		components: {
			NormalPage,
			ParallaxImage,
			InfoFooter
		}
	}
</script>