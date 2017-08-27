from django.core.management.base import BaseCommand, CommandError
from dpmfa import models as dbm
from django.contrib.auth.models import User

class ModelCopier(object):

    @staticmethod
    def copy_model(model_ref):
        model_copy = dbm.model.objects.get(pk=model_ref.pk)
        model_copy.pk = None
        model_copy.save()

        compartment_by_ref_pk = {}

        #flow_compartment_by_ref_pk= {}
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

        sink_by_ref_pk = {}
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

        stock_by_ref_pk = {}
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

        print('hello')
        for release_ref in dbm.fixed_rate_release.objects.filter(stock__model=model_ref):
            release_copy = dbm.fixed_rate_release(

            )







        """
        for flow_compartment_ref in dbm.flow_compartment.objects.filter(mode=model_ref):
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
        """

        """
        flow_compartment_copies = [
            dbm.flow_compartment(
                model=model_copy,
                name=flow_compartment_ref.name,
                description=flow_compartment_ref.description,
                evt_changed=flow_compartment_ref.evt_changed,
                evt_created=flow_compartment_ref.evt_created,
                log_inflows=flow_compartment_ref.log_inflows,
                categories=flow_compartment_ref.categories,
                adjust_outgoing_tcs=flow_compartment_ref.adjust_outgoing_tcs,
                log_outflows=flow_compartment_ref.log_outflows
            ) for flow_compartment_ref in dbm.flow_compartment.objects.filter(model=model_ref)
        ]
        for flow_compartment_copy in flow_compartment_copies:
            flow_compartment_copy.save()

        stocks = [
            dbm.flow_compartment(
                model=model_copy,
                name=stock_ref.name,
                description=stock_ref.description,
                evt_changed=stock_ref.evt_changed,
                evt_created=stock_ref.evt_created,
                log_inflows=stock_ref.log_inflows,
                categories=stock_ref.categories,
                adjust_outgoing_tcs=stock_ref.adjust_outgoing_tcs,
                log_outflows=stock_ref.log_outflows,
                local_release=
            ) for stock_ref in dbm.stock.objects.filter(model=model_ref)
        ]
        for flow_compartment_copy in flow_compartment_copies:
            flow_compartment_copy.save()
        """


class Command(BaseCommand):

    def handle(self, *args, **options):
        model1 = dbm.model.objects.get(pk=1)
        ModelCopier.copy_model(model1)
        models = dbm.model.objects.all()
        for model in models:
            print(model.pk)
            print(model.compartments.all())


