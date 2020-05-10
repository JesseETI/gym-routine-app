const TOKEN_KEY = 'user-token'

const tokenService = {
    getToken() {
        return localStorage.getItem(TOKEN_KEY)
    }
}



export {
    tokenService
}