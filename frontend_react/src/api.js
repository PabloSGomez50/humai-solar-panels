import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/';

const axiosI = axios.create({
    baseURL: API_URL,
    headers: {'Content-Type': 'application/json'},
})

export default axiosI;