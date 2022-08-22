import axios from 'axios'

export default () => new Promise ((resolve, reject) => {
	axios
	.post(`${process.env.VUE_APP_URL}stadistic`,
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
		} 
	})
	.catch(error => {
		reject(error)
	})
})