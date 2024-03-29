import { fetchMovies } from "../utils/functions.js";

/**
 * Movie data component
 * @returns A div element with the movies
 */
export function Movies() {
    let element = document.createElement('div');
    let actualPage
    window.document.title = 'Peliculas'
    
    const nxtBtn = window.document.getElementById('nextBtn')
    const backBtn = window.document.getElementById('backBtn')

    async function getMovies (){    
        try {

            const url = new URLSearchParams(window.location.hash.split('peliculas')[1])
            actualPage = url.get('page')
            
            nxtBtn.onclick = async function () {
                actualPage++            
                const newPage = `http://127.0.0.1:5500/index.html#/peliculas?page=${actualPage}`
                window.location.href = newPage
            }
        
            backBtn.onclick = async function () {
                if (actualPage > 1) {
                    actualPage--
                    const newPage = `http://127.0.0.1:5500/index.html#/peliculas?page=${actualPage}`
                    window.location.href = newPage
                }
            }
    
            let data = await fetchMovies(actualPage)
            
            let html = ""
            
            for(let i = 0; i < data.results.length;i++){
                const movie = data.results[i]
                const date = movie.release_date.split('-')[0]
                html += `
                    <section class="card-section" id="b${i}">
                        <img class="movie-img" src="https://image.tmdb.org/t/p/w500/${movie.backdrop_path}" alt="${movie.title}">
                        <div class="description-div">
                            <div class="title">
                                <h1>${movie.title}</h1>
                                <p>${movie.overview}</p>
                            </div>
                            <h3>Valoración</h3>
                            <p><b>${movie.vote_average}</b></p>
                        </div>
    
                        <div id="m${movie.id}" class="modal">
    
                            <div class="modal-content">
                                <span id="close${movie.id}" class="close">&times;</span>
                                <img src="https://image.tmdb.org/t/p/w500/${movie.poster_path}" alt="${movie.title}">
                                <div class="description-div">
                                    <div class="title">
                                        <h1>${movie.title} (${date})</h1>
                                        <p>${movie.overview}</p>
                                    </div>
                                    <h3>Valoración</h3>
                                    </br>
                                    <p><b>${movie.vote_average}</b></p>
                                    <h4>Fecha de lanzamiento: ${movie.release_date}</h4>
                                </div>
                            </div>
    
                        </div>
                    </section>
                `
            }
            element.innerHTML = html
    
            for(let i = 0; i < data.results.length;i++){
                const movie = data.results[i]
                
                let btn = element.querySelector(`#b${i}`)
    
                let modal = element.querySelector(`#m${movie.id}`);
            
                let span = element.querySelector(`#close${movie.id}`);
            
                btn.onclick = function() {
                    modal.style.display = "block";
                    window.document.title = `Peliculas | ${movie.title}`
                }
            
                span.onclick = function() {
                    modal.style.display = "none";
                }
            
                window.addEventListener('click', (e) => {
                    if (e.target == modal) {
                        modal.style.display = "none";
                        window.document.title = 'Peliculas'
                    }
                })
            }
        } catch (error) {
            console.error(`Hubo un error ${error}`)
        }
    }
    getMovies()
    
    
    return element
}
