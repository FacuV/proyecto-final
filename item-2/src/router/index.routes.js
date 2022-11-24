import { Movies } from "../views/Movies.js"
import Series from "../views/Series.js"

const root = document.getElementById('root')

const router = (route) => {
    root.innerHTML = ""
    switch(route) {
        case '#/':
            console.log('Main')
            break
        case '#/peliculas': {
            root.appendChild(Movies())
            break
        }   
        case '#/series':
            root.appendChild(Series())
            break

    }
}

export {router};