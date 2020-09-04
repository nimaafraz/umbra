# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: umbra.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client

if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
from umbra.common.protobuf import umbra_pb2


class BrokerBase(abc.ABC):
    @abc.abstractmethod
    async def Execute(
        self, stream: "grpclib.server.Stream[umbra_pb2.Config, umbra_pb2.Report]"
    ) -> None:
        pass

    @abc.abstractmethod
    async def Measure(
        self, stream: "grpclib.server.Stream[umbra_pb2.Evaluation, umbra_pb2.Status]"
    ) -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/umbra.Broker/Execute": grpclib.const.Handler(
                self.Execute,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Config,
                umbra_pb2.Report,
            ),
            "/umbra.Broker/Measure": grpclib.const.Handler(
                self.Measure,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Evaluation,
                umbra_pb2.Status,
            ),
        }


class BrokerStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Execute = grpclib.client.UnaryUnaryMethod(
            channel, "/umbra.Broker/Execute", umbra_pb2.Config, umbra_pb2.Report,
        )
        self.Measure = grpclib.client.UnaryUnaryMethod(
            channel, "/umbra.Broker/Measure", umbra_pb2.Evaluation, umbra_pb2.Status,
        )


class ScenarioBase(abc.ABC):
    @abc.abstractmethod
    async def Establish(
        self, stream: "grpclib.server.Stream[umbra_pb2.Workflow, umbra_pb2.Status]"
    ) -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/umbra.Scenario/Establish": grpclib.const.Handler(
                self.Establish,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Workflow,
                umbra_pb2.Status,
            ),
        }


class ScenarioStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Establish = grpclib.client.UnaryUnaryMethod(
            channel, "/umbra.Scenario/Establish", umbra_pb2.Workflow, umbra_pb2.Status,
        )


class MonitorBase(abc.ABC):
    @abc.abstractmethod
    async def Listen(
        self, stream: "grpclib.server.Stream[umbra_pb2.Instruction, umbra_pb2.Snapshot]"
    ) -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/umbra.Monitor/Listen": grpclib.const.Handler(
                self.Listen,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Instruction,
                umbra_pb2.Snapshot,
            ),
        }


class MonitorStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Listen = grpclib.client.UnaryUnaryMethod(
            channel, "/umbra.Monitor/Listen", umbra_pb2.Instruction, umbra_pb2.Snapshot,
        )


class AgentBase(abc.ABC):
    @abc.abstractmethod
    async def Probe(
        self, stream: "grpclib.server.Stream[umbra_pb2.Instruction, umbra_pb2.Snapshot]"
    ) -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/umbra.Agent/Probe": grpclib.const.Handler(
                self.Probe,
                grpclib.const.Cardinality.UNARY_UNARY,
                umbra_pb2.Instruction,
                umbra_pb2.Snapshot,
            ),
        }


class AgentStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Probe = grpclib.client.UnaryUnaryMethod(
            channel, "/umbra.Agent/Probe", umbra_pb2.Instruction, umbra_pb2.Snapshot,
        )
