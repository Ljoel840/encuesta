import axios from 'axios'

export default (entrada) => new Promise ((resolve, reject) => {
	axios
	.post(`${process.env.VUE_APP_URL}submitted`, entrada,
	{
		dataType: 'json',
		xhrFields: {
			withCredentials: true
		},
		crossDomain: true,
		contentType: 'application/json; charset=utf-8'
	}
	)
	.then(response => {
		if (!response.data) {
			reject('No hay retorno del backend')
		} else {
			resolve(response.data)  
			console.log(response.data)          
		} 
	})
	.catch(error => {
		reject(error)
	})
})