export const fetchMovies = async () => {
    const API_KEY = '052ab590ffacf9a4152647f0564e9d04'
    const url = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=es-AR&page=1`
    
    fetch(url)
    .then(res => res.json())
    .then(data => {
        window.localStorage.setItem('Data', JSON.stringify(data))
    })
}