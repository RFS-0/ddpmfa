(function() {
    jQuery(document).ready(function() {
        jQuery('[data-toggle="tooltip"]').tooltip();
    });
})();


jsPlumb.ready(function() {
    jQuery(document).ready(function() {
        jQuery('.dpmfa-model-designer').each(function() {
            var containerQ = jQuery(this);
            jsPlumb.setContainer(containerQ);

            var endpointConfig = {
                isSource:true,
                isTarget:true,
                connector: ['Straight'],
                maxConnections: -1
            };

            var comp1 = jQuery('<div class="compartment">A compartment</div>')
            comp1.css({ left: 30 + 'px', top: 60 + 'px' });
            containerQ.append(comp1);
            jsPlumb.draggable(comp1);

            jsPlumb.addEndpoint(comp1, { anchor:'Left' }, endpointConfig);
            jsPlumb.addEndpoint(comp1, { anchor:'Right' }, endpointConfig);

            var comp2 = jQuery('<div class="compartment">A second compartment</div>')
            comp2.css({ left: 290 + 'px', top: 160 + 'px' });
            containerQ.append(comp2);
            jsPlumb.draggable(comp2);

            jsPlumb.addEndpoint(comp2, { anchor:'Left' }, endpointConfig);
            jsPlumb.addEndpoint(comp2, { anchor:'Right' }, endpointConfig);

            var comp3 = jQuery('<div class="compartment">A third compartment</div>')
            comp3.css({ left: 590 + 'px', top: 60 + 'px' });
            containerQ.append(comp3);
            jsPlumb.draggable(comp3);

            jsPlumb.addEndpoint(comp3, { anchor:'Left' }, endpointConfig);
            jsPlumb.addEndpoint(comp3, { anchor:'Right' }, endpointConfig);


            jsPlumb.connect({
                connector: ["Straight"],
                source:comp1,
                target: comp2,
                anchor: ["Left", "Right"],
                endpoint:"Dot",
                overlays:[
                    ["Arrow", { width:12, length:12, location:0.67 }]
                ]
            });

            jsPlumb.connect({
                connector: ["Straight"],
                source:comp2,
                target: comp3,
                anchor: ["Left", "Right"],
                endpoint:"Dot",
                overlays:[
                    ["Arrow", { width:12, length:12, location:0.67 }]
                ]
            });
        });
    });
});

