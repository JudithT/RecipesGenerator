
import Recipes from './recipes'

class RecipeByIngredients extends React.Component {
    constructor(props){
        super(props);
    }

    render(){
        const url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients="
        return(         
            <Recipes url={url}/>
        
        )
    }
}

ReactDOM.render(<RecipeByIngredients />, document.getElementById('root'));

