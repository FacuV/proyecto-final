const API_KEY = '052ab590ffacf9a4152647f0564e9d04'

export const fetchMovies = async (page) => {
    const url = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=es-AR&page=${page}`
    
    const data = await fetch(url)
    return data.json()
}


export const fetchSeries = async (page) => {
    const url = `https://api.themoviedb.org/3/tv/popular?api_key=${API_KEY}&language=es-AR&page=${page}`
    
    const data = await fetch(url)
    return data.json()
}