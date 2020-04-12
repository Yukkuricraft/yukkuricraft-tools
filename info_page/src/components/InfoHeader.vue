<template>
	<nav id="top-navbar" class="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
		<slot name="top"></slot>
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
				aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
		</button>

		<div class="collapse navbar-collapse" id="navbarSupportedContent">
			<ul class="navbar-nav mr-auto">
				<router-link :to="{name: 'info'}" v-slot="{ href, navigate, isExactActive }">
					<li class="nav-item" :class="[isExactActive && 'active']">
						<a class="nav-link" :href="href" @click="navigate">Info</a>
					</li>
				</router-link>
				<router-link :to="{name: 'ranks_staff'}" v-slot="{ href, navigate, isExactActive }">
					<li class="nav-item" :class="[isExactActive && 'active']">
						<a class="nav-link" :href="href" @click="navigate">Ranks and Staff</a>
					</li>
				</router-link>
				<router-link :to="{name: 'rules'}" v-slot="{ href, navigate, isExactActive }">
					<li class="nav-item" :class="[isExactActive && 'active']">
						<a class="nav-link" :href="href" @click="navigate">Rules</a>
					</li>
				</router-link>
				<router-link :to="{name: 'commands'}" v-slot="{ href, navigate, isExactActive }">
					<li class="nav-item" :class="[isExactActive && 'active']">
						<a class="nav-link" :href="href" @click="navigate">Commands</a>
					</li>
				</router-link>
				<li class="nav-item"><a class="nav-link" href="https://yukkuricraft.net">Forums</a></li>
			</ul>
		</div>

		<div class="navbar-text">
			<div class="form-inline">
				<label class="m-1" for="locale">Locale: </label>
				<select class="form-control p-0 h-100" id="locale" v-model="locale">
					<option value="en">English</option>
					<option value="ja">Japanese</option>
				</select>
			</div>
		</div>
		<slot name="bottom"></slot>
	</nav>
</template>

<script>

	export default {
		data() {
			let preferredLanguage = window.navigator.language.slice(0, 2);
			if (typeof this.$i18n !== 'undefined') {
				this.$i18n.locale = preferredLanguage;
			}
			return {
				locale: preferredLanguage
			}
		},
		watch: {
			locale(val) {
				if (typeof this.$i18n != 'undefined') {
					this.$i18n.locale = val
				}
			}
		}
	}
</script>
