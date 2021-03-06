# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the Apache 2.0 License.

from enum import Enum


class ProposalNotCreated(Exception):
    def __init__(self, response):
        super(ProposalNotCreated, self).__init__()
        self.response = response


class ProposalNotAccepted(Exception):
    def __init__(self, proposal):
        super(ProposalNotAccepted, self).__init__()
        self.proposal = proposal


# Values defined in node/proposals.h
class ProposalState(Enum):
    Open = "OPEN"
    Accepted = "ACCEPTED"
    Withdrawn = "WITHDRAWN"
    Rejected = "REJECTED"
    Failed = "FAILED"


class Proposal:
    def __init__(
        self, proposer_id, proposal_id, state, has_proposer_voted_for=True,
    ):
        self.proposer_id = proposer_id
        self.proposal_id = proposal_id
        self.state = state
        self.has_proposer_voted_for = has_proposer_voted_for
        self.votes_for = 1 if self.has_proposer_voted_for else 0
        self.vote_for = {"ballot": {"text": "return true"}}

    def increment_votes_for(self):
        self.votes_for += 1
