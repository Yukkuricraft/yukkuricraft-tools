<template>
	<div class="sidebar-wrapper">
		<nav class="sidebar" :class="{active: sidebarActive}">
			<slot name="sidebar"></slot>
		</nav>

		<div class="sidebar-content" :class="{active: sidebarActive}">
			<info-header :in-container="false">
				<template v-slot:top>
					<button @click="sidebarActive = !sidebarActive" class="btn" type="button" aria-controls="sidebar-nav"
							aria-expanded="false" aria-label="Toggle sidebar">
						<i class="text-white fas fa-align-left"></i>
					</button>
				</template>
			</info-header>

			<parallax-image :class="parallaxClass">
				<slot name="parallax"></slot>
			</parallax-image>

			<div class="container">
				<slot></slot>

				<info-footer></info-footer>
			</div>
		</div>
	</div>
</template>

<script>
	import InfoHeader from "../components/InfoHeader";
	import InfoFooter from "../components/InfoFooter";
	import ParallaxImage from "../components/ParallaxImage";

	export default {
		components: {
			InfoHeader,
			InfoFooter,
			ParallaxImage
		},
		props: {
			parallaxClass: String
		},
		data() {
			return {
				sidebarActive: false
			}
		}
	}
</script>