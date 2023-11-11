htmx.onLoad(function() {  
    const components = document.getElementById("ec-components");
    if (components) {
        const sortableComponents = Sortable.create(components, {
            animation: 150,
            group: "components",
            ghostClass: "sortable-ghost",
            // handle: ".ec-compontent-handle",
            direction: "vertical",
            filter: ".last-element",
        });
    };

    const newComponents = document.getElementById("ec-new-components");
    if (newComponents) {
        const sortableNewComponents = Sortable.create(newComponents, {
            animation: 150,
            group: "components",
            ghostClass: "sortable-ghost",
            // handle: ".ec-compontent-handle",
            direction: "vertical",
            sort: false,
            group: {
                name: 'components',
                pull: 'clone',
                put: false,
            },            
        });   
    };

    
    function adjustWidthLeft() {
        const parent = document.getElementById("ec-new-components-parent");
        const parentWidth = parent.offsetWidth;
        
        const component = document.getElementById("ec-new-components");
        component.setAttribute("style", "width: " + parentWidth + "px;");
    };

    function adjustWidthRight() {
        const parent = document.getElementById("ec-edit-form-parent");
        const parentWidth = parent.offsetWidth;
        
        const component = document.getElementById("ec-edit-form");
        component.setAttribute("style", "width: " + parentWidth + "px;");
    };

    // adjustWidthLeft();
    // adjustWidthRight();

})


