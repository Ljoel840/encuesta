const { defineConfig } = require('@vue/cli-service')


const test = {
	apiUrl: "http://localhost:5000/",
};

const prod = {
	apiUrl: "http://localhost:5000/", //Colocar url de producción de las apis
}

const amb = process.env.NODE_ENV === "development"
	? test.apiUrl
	: prod.apiUrl;

process.env.VUE_APP_URL = amb

module.exports = defineConfig({
	transpileDependencies: true,
	productionSourceMap: false,
})
