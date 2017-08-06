Author: <a href="mailto:nikolaus.bornhoeft@empa.ch">Nikolaus Bornhoeft</a>
Institution: Empa St. Gallen,  <a href="http://www.empa.ch/plugin/template/empa/*/6692/---/l=1">Environmental Risk Assessment and Management Group</a>

The dpmfa framework supports the generation and use of dynamic probabilistic material flow models.

It enables to model of time dynamic flow models on a period base.
Incomplete knowledge about the true values of a system parameter about the absolute inflows to the system over time and the
relative transfer coefficients for the flows between the system compartments is represented as Bayesian probability distribution.
It is propagated to dependent model variables using Monte-Carlo simulation, while ensuring mass-balance in every element of the Monte-Carlo sample.

The dpmfa_simulator package holds a simulation infrastructure providing a ready-to-use simulator class and a set of model components that need to be implemented and assembled to represent system specific knowledge.
Also an example package is included that contains a small example model and a runner file to illustrate the use of the dpmfa simulator.

We are currently preparing a publication about the development and application of the simulation framework. It will be linked as soon, as it is published.
Its main aim is to provide means for environmental exporsure assessment modeling of anthropogenic pollutants. The possibilities and limitations of existing tools is discussed <a href="http://www.bibsonomy.org/bibtex/2bb12d820eaf0014c54087c510f2de8cf/dblp/">here </a>.

The dpmfa-framework was created within the <a href="http://www.marina-fp7.eu/">"Marina - Managing the Risk of Nanomaterials" </a> Framework of the European Union

