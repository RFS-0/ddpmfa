from dpmfa import models as dbm

class ModelCopier(object):

    """
    Copies the reference model `model_ref` and saves the copy in the database.
    Returns the copy of the model. Expects a `model` as input and returns a
    `model_instance`.
    """
    @staticmethod
    def copy_model(model_ref):
        model_copy = dbm.model_instance(
            project=model_ref.project,
            name=model_ref.name,
            description=model_ref.description,
            seed=model_ref.seed,
            evt_created=model_ref.evt_created,
            evt_changed=model_ref.evt_changed,
            prototype_model=model_ref
        )
        model_copy.save()

        compartment_by_ref_pk = {}

        for flow_compartment_ref in dbm.flow_compartment.objects.filter(model=model_ref):
            if dbm.stock.objects.filter(pk=flow_compartment_ref.pk).count() == 0:
                flow_compartment_copy = dbm.flow_compartment(
                    model=model_copy,
                    name=flow_compartment_ref.name,
                    description=flow_compartment_ref.description,
                    evt_changed=flow_compartment_ref.evt_changed,
                    evt_created=flow_compartment_ref.evt_created,
                    log_inflows=flow_compartment_ref.log_inflows,
                    categories=flow_compartment_ref.categories,
                    adjust_outgoing_tcs=flow_compartment_ref.adjust_outgoing_tcs,
                    log_outflows=flow_compartment_ref.log_outflows
                )
                flow_compartment_copy.save()
                compartment_by_ref_pk[flow_compartment_ref.pk] = flow_compartment_copy

        for sink_ref in dbm.sink.objects.filter(model=model_ref):
            sink_copy = dbm.sink(
                model=model_copy,
                name=sink_ref.name,
                description=sink_ref.description,
                evt_changed=sink_ref.evt_changed,
                evt_created=sink_ref.evt_created,
                log_inflows=sink_ref.log_inflows,
                categories=sink_ref.categories
            )
            sink_copy.save()
            compartment_by_ref_pk[sink_ref.pk] = sink_copy

        for stock_ref in dbm.stock.objects.filter(model=model_ref):
            stock_copy = dbm.stock(
                model=model_copy,
                name=stock_ref.name,
                description=stock_ref.description,
                evt_changed=stock_ref.evt_changed,
                evt_created=stock_ref.evt_created,
                log_inflows=stock_ref.log_inflows,
                categories=stock_ref.categories,
                adjust_outgoing_tcs=stock_ref.adjust_outgoing_tcs,
                log_outflows=stock_ref.log_outflows
            )
            stock_copy.save()
            compartment_by_ref_pk[stock_ref.pk] = stock_copy

        aggregated_transfer_by_ref_pk = {}
        aggregated_transfer_refs = dbm.aggregated_transfer.objects.filter(target__model=model_ref)
        for transfer_ref in aggregated_transfer_refs:
            transfer_copy = dbm.aggregated_transfer(
                target=compartment_by_ref_pk[transfer_ref.target.pk] if not transfer_ref.target is None else None,
                source_flow_compartment=compartment_by_ref_pk[transfer_ref.source_flow_compartment.pk] if not transfer_ref.source_flow_compartment is None else None,
                name=transfer_ref.name,
                priority=transfer_ref.priority,
                current_tc=transfer_ref.current_tc,
                weight=transfer_ref.weight,
                weights=transfer_ref.weights
            )
            transfer_copy.save()
            aggregated_transfer_by_ref_pk[transfer_ref.pk] = transfer_copy

        for transfer_ref in aggregated_transfer_refs:
            if not transfer_ref.belongs_to_aggregated_transfer is None:
                transfer_copy = aggregated_transfer_by_ref_pk[transfer_ref.pk]
                transfer_copy.belongs_to_aggregated_transfer = aggregated_transfer_by_ref_pk[transfer_ref.belongs_to_aggregated_transfer.pk]
                transfer_copy.save()

        for transfer_ref in dbm.constant_transfer.objects.filter(target__model=model_ref):
            transfer_copy = dbm.constant_transfer(
                target=compartment_by_ref_pk[transfer_ref.target.pk] if not transfer_ref.target is None else None,
                source_flow_compartment=compartment_by_ref_pk[transfer_ref.source_flow_compartment.pk] if not transfer_ref.source_flow_compartment is None else None,
                belongs_to_aggregated_transfer=aggregated_transfer_by_ref_pk[transfer_ref.belongs_to_aggregated_transfer.pk] if not transfer_ref.belongs_to_aggregated_transfer is None else None,
                name=transfer_ref.name,
                priority=transfer_ref.priority,
                current_tc=transfer_ref.current_tc,
                weight=transfer_ref.weight,
                value=transfer_ref.value
            )
            transfer_copy.save()

        for transfer_ref in dbm.random_choice_transfer.objects.filter(target__model=model_ref):
            transfer_copy = dbm.random_choice_transfer(
                target=compartment_by_ref_pk[transfer_ref.target.pk] if not transfer_ref.target is None else None,
                source_flow_compartment=compartment_by_ref_pk[transfer_ref.source_flow_compartment.pk] if not transfer_ref.source_flow_compartment is None else None,
                belongs_to_aggregated_transfer=aggregated_transfer_by_ref_pk[transfer_ref.belongs_to_aggregated_transfer.pk] if not transfer_ref.belongs_to_aggregated_transfer is None else None,
                name=transfer_ref.name,
                priority=transfer_ref.priority,
                current_tc=transfer_ref.current_tc,
                weight=transfer_ref.weight,
                sample=transfer_ref.sample
            )
            transfer_copy.save()

        for transfer_ref in dbm.stochastic_transfer.objects.filter(target__model=model_ref):
            transfer_copy = dbm.stochastic_transfer(
                target=compartment_by_ref_pk[transfer_ref.target.pk] if not transfer_ref.target is None else None,
                source_flow_compartment=compartment_by_ref_pk[transfer_ref.source_flow_compartment.pk] if not transfer_ref.source_flow_compartment is None else None,
                belongs_to_aggregated_transfer=aggregated_transfer_by_ref_pk[transfer_ref.belongs_to_aggregated_transfer.pk] if not transfer_ref.belongs_to_aggregated_transfer is None else None,
                name=transfer_ref.name,
                priority=transfer_ref.priority,
                current_tc=transfer_ref.current_tc,
                weight=transfer_ref.weight,
                parameters=transfer_ref.parameters,
                function=transfer_ref.function
            )
            transfer_copy.save()

        for transfer_ref in dbm.stochastic_transfer.objects.filter(target__model=model_ref):
            transfer_copy = dbm.stochastic_transfer(
                target=compartment_by_ref_pk[transfer_ref.target.pk] if not transfer_ref.target is None else None,
                source_flow_compartment=compartment_by_ref_pk[transfer_ref.source_flow_compartment.pk] if not transfer_ref.source_flow_compartment is None else None,
                belongs_to_aggregated_transfer=aggregated_transfer_by_ref_pk[transfer_ref.belongs_to_aggregated_transfer.pk] if not transfer_ref.belongs_to_aggregated_transfer is None else None,
                name=transfer_ref.name,
                priority=transfer_ref.priority,
                current_tc=transfer_ref.current_tc,
                weight=transfer_ref.weight,
                parameters=transfer_ref.parameters
            )
            transfer_copy.save()



        for release_ref in dbm.fixed_rate_release.objects.filter(stock__model=model_ref):
            release_copy = dbm.fixed_rate_release(
                name=release_ref.name,
                delay=release_ref.delay,
                stock=compartment_by_ref_pk[release_ref.stock.pk],
                release_rate=release_ref.release_rate
            )
            release_copy.save()
            compartment_by_ref_pk[release_ref.stock.pk].local_release = release_copy
            compartment_by_ref_pk[release_ref.stock.pk].save()

        for release_ref in dbm.list_release.objects.filter(stock__model=model_ref):
            release_copy = dbm.list_release(
                name=release_ref.name,
                delay=release_ref.delay,
                stock=compartment_by_ref_pk[release_ref.stock.pk],
                release_rate_list=release_ref.release_rate_list
            )
            release_copy.save()
            compartment_by_ref_pk[release_ref.stock.pk].local_release = release_copy
            compartment_by_ref_pk[release_ref.stock.pk].save()

        for release_ref in dbm.function_release.objects.filter(stock__model=model_ref):
            release_copy = dbm.function_release(
                name=release_ref.name,
                delay=release_ref.delay,
                stock=compartment_by_ref_pk[release_ref.stock.pk],
                release_function=release_ref.release_function,
                function_parameters=release_ref.function_parameters
            )
            release_copy.save()
            compartment_by_ref_pk[release_ref.stock.pk].local_release = release_copy
            compartment_by_ref_pk[release_ref.stock.pk].save()



        for inflow_ref in dbm.external_list_inflow.objects.filter(target__model=model_ref):
            inflow_copy = dbm.external_list_inflow(
                target=compartment_by_ref_pk[inflow_ref.target.pk],
                name=inflow_ref.name,
                start_delay=inflow_ref.start_delay,
                derivation_distribution=inflow_ref.derivation_distribution,
                derivation_parameters=inflow_ref.derivation_parameters,
                derivation_factor=inflow_ref.derivation_factor
            )
            inflow_copy.save()

            for period_inflow_ref in dbm.fixed_value_inflow.objects.filter(external_list_inflow=inflow_ref):
                period_inflow_copy = dbm.fixed_value_inflow(
                    external_list_inflow=inflow_copy,
                    current_value=period_inflow_ref.current_value,
                    period=period_inflow_ref.period,
                    value=period_inflow_ref.value
                )
                period_inflow_copy.save()

            for period_inflow_ref in dbm.stochastic_function_inflow.objects.filter(external_list_inflow=inflow_ref):
                period_inflow_copy = dbm.stochastic_function_inflow(
                    external_list_inflow=inflow_copy,
                    current_value=period_inflow_ref.current_value,
                    period=period_inflow_ref.period,
                    pdf=period_inflow_ref.pdf,
                    parameter_values=period_inflow_ref.parameter_values
                )
                period_inflow_copy.save()

            for period_inflow_ref in dbm.random_choice_inflow.objects.filter(external_list_inflow=inflow_ref):
                period_inflow_copy = dbm.random_choice_inflow(
                    external_list_inflow=inflow_copy,
                    current_value=period_inflow_ref.current_value,
                    period=period_inflow_ref.period,
                    sample=period_inflow_ref.sample
                )
                period_inflow_copy.save()

        for inflow_ref in dbm.external_function_inflow.objects.filter(target__model=model_ref):
            inflow_copy = dbm.external_function_inflow(
                target=compartment_by_ref_pk[inflow_ref.target.pk],
                name=inflow_ref.name,
                start_delay=inflow_ref.start_delay,
                derivation_distribution=inflow_ref.derivation_distribution,
                derivation_parameters=inflow_ref.derivation_parameters,
                derivation_factor=inflow_ref.derivation_factor,
                inflow_function=inflow_ref.inflow_function,
                function_parameters=inflow_ref.function_parameters
            )
            inflow_copy.save()

            for period_inflow_ref in dbm.fixed_value_inflow.objects.filter(external_function_inflow=inflow_ref):
                period_inflow_copy = dbm.fixed_value_inflow(
                    external_function_inflow=inflow_copy,
                    current_value=period_inflow_ref.current_value,
                    period=period_inflow_ref.period,
                    value=period_inflow_ref.value
                )
                period_inflow_copy.save()

            for period_inflow_ref in dbm.stochastic_function_inflow.objects.filter(external_function_inflow=inflow_ref):
                period_inflow_copy = dbm.stochastic_function_inflow(
                    external_function_inflow=inflow_copy,
                    current_value=period_inflow_ref.current_value,
                    period=period_inflow_ref.period,
                    pdf=period_inflow_ref.pdf,
                    parameter_values=period_inflow_ref.parameter_values
                )
                period_inflow_copy.save()

            for period_inflow_ref in dbm.random_choice_inflow.objects.filter(external_function_inflow=inflow_ref):
                period_inflow_copy = dbm.random_choice_inflow(
                    external_function_inflow=inflow_copy,
                    current_value=period_inflow_ref.current_value,
                    period=period_inflow_ref.period,
                    sample=period_inflow_ref.sample
                )
                period_inflow_copy.save()

        return model_copy