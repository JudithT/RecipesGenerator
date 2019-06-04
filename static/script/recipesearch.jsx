const get = axios.create({
    headers: {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "0fd28a9296msh61f75fee9171434p1d6995jsn9f02884e2ae5"
    }
    })

    const url = terms => `https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients=${terms}`

    const Recipe = recipe => {
    return (
    <div>
        <div>
            <img src={recipe.image}/>
           
        </div>
        <div>
            {recipe.videos && recipe.videos.length && recipe.videos[0].youTubeId}
        {recipe.videos && recipe.videos.length && <iframe id="video" width="420" height="315" src={`https://www.youtube.com/embed/${recipe.videos[0].youTubeId}`} frameborder="0" allowfullscreen></iframe>}
        </div>
        <div>
             recipe title: {recipe.title}
        </div>


        <div>
            USED INGREDIENTS:  {recipe.usedIngredients.map(Ingredient)}
        </div>
       
        <div>Missing Ingredients:  {recipe.missedIngredients.map(Ingredient)}</div>
        {recipe.instruction && <div>{recipe.instruction}</div>}
    </div> 

    )
    }

    const Ingredient = ingredient => <li>{ingredient.name}<img src={ingredient.image} /></li>;
        

    const App = () => {
    const [query, setQuery] = React.useState('apples,sugar,flour')
    const [recipes, setRecipes] = React.useState([])

    
    React.useEffect(()=> {
    const fetch = async () => {
        console.log(query)
        const result = await get(url(query));
        setRecipes(result.data);
    }
    fetch()
    }, []
    );

    const f = () => new Promise((resolve, reject) => resolve).then

    const onSubmit = async event => {
    event.preventDefault();
    console.log(query)
    const result = await get(url(query)); // wait until the promise finishes and then passed it to the function below 
    console.log("=========>,",result.data)
    for(let i=0; i<result.data.length; i++){
        const id = result.data[i].id
        const title = result.data[i].title
        const instructionUrl = `https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/${id}/information`
        const videoUrl = `https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search?query=${title}&includeingredients=${query}`
        const instructionResponse = await get(instructionUrl)
        const videoResponse = await get(videoUrl)
        result.data[i] = {...result.data[i], ...instructionResponse.data, ...videoResponse.data}
        
    }
    console.log("=== after", result.data)

    setRecipes(result.data);
    }

    return (
        <div className="App">
        <header className="App-header">
            <form onSubmit={onSubmit}>
            <input type="text" value={query} onChange={event => setQuery(event.target.value)}
    />
            <button type="submit">Search</button>
            </form>
            <ul>
            {recipes.map(Recipe)}
            </ul>
        </header>
        </div>
    );
    }
        
    ReactDOM.render(<App />, document.getElementById('root'));