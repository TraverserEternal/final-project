export const teams = (state = [], action) => {
    switch (action.type) {
        case 'setTeams':
            return action.data
        default:
            return state
    }
}