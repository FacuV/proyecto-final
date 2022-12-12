import { Main } from "../views/Main.js"
import { Movies } from "../views/Movies.js"
import { Series } from "../views/Series.js"

const root = document.getElementById('root')

const router = (route) => {
    root.innerHTML = ""
    const url = new URLSearchParams(window.location.hash.split('?')[1])
    const page = url.get('page')
    switch(route) {
        case '#/':
            root.appendChild(Main())
            break
        case `#/peliculas?page=${page}`: {
            root.appendChild(Movies(page))
            break
        }   
        case `#/series?page=${page}`:
            root.appendChild(Series(page))
            break

    }
}

export {router};