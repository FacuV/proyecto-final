import { fetchMovies } from "../utils/functions.js";

export function Movies() {
    let element = document.createElement('div');
    
    async function getMovies (){    
        let data
        const isDataInLocalStorage = JSON.parse(window.localStorage.getItem('Data')) ? true : false
        
        if(isDataInLocalStorage){
            data = JSON.parse(window.localStorage.getItem('Data'))
        } else {
            fetchMovies()
            .then(
                setTimeout(() => { window.location.reload() }, 1000)
            )
            
        }
        
        let html = ""
        
        for(let i = 0; i < data.results.length;i++){
            const movie = data.results[i]
            html += `
                <section class="card-section">
                    <img class="movie-img" src="https://image.tmdb.org/t/p/w500/${movie.backdrop_path}" alt="${movie.title}">
                    <div class="description-div">
                        <div class="title">
                            <h1>${movie.title}</h1>
                            <p>${movie.overview}</p>
                        </div>
                        <h3>Valoración</h3>
                        <p><b>${movie.vote_average}</b></p>
                    </div>
                </section>
            `
        }
        element.innerHTML = html
    }
    getMovies()
    
    return element
}
