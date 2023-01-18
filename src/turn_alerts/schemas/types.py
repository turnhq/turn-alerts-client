from enum import Enum


class UserTypeEnum(str, Enum):
    partner = "partner"
    recruitment_marketing_partner = "recruitment_marketing_partner"


class ObjectTypeEnum(str, Enum):
    advise_job = "advise_job"
    s3_upload = "s3_upload"
    export_request = "export_request"
    cohort = "cohort"
    invitation = "invitation"
    background_check = "background_check"
    single_invitation = "single_invitation",
    bulk_upload = "bulk_upload"



class AlertTypeEnum(str, Enum):
    EXPORT_REQUEST_FULFILLED = "EXPORT_REQUEST_FULFILLED"
    EXPORT_REQUEST_FAILED = "EXPORT_REQUEST_FAILED"
    IMPORT_START_PROCESSING = "START_PROCESSING"
    IMPORT_PROCESSING_ERROR = "PROCESSING_ERROR"
    IMPORT_FINISHED_PROCESS = "FINISHED_PROCESS"

    BGC_APPROVED = "background_check_approved"
    BGC_COMPLIANCE_REVIEW = "background_check_compliance_review"
    BGC_CONSENT = "background_check_consent"
    BGC_CONSIDER = "background_check_consider"
    BGC_EMAILED = "background_check_emailed"
    BGC_FIRST_NOTICE = "background_check_first_notice"
    BGC_INITIATED = "background_check_initiated"
    BGC_PROCESSING = "background_check_processing"
    BGC_REJECTED = "background_check_rejected"
    BGC_REVIEW = "background_check_review"
    BGC_SECOND_NOTICE = "background_check_second_notice"
    BGC_VERIFYING = "background_check_verifying"
    BGC_WITHDRAWN = "background_check_withdrawn"

    COHORT_NEW_APPLIES_COUNT = "cohort_new_applications_count"

    CANDIDATE_REACHED_INTERVIEW_STAGE = "candidate_reached_interview_stage"
    CANDIDATE_REACHED_HIRED_STAGE = "candidate_reached_hired_stage"

    READY_ACCOUNT_DETAILS_UPDATE = "ready_account_details_update"
    ADVISE_ACCOUNT_DETAILS_UPDATE = "advise_account_details_update"

    SINGLE_INVITE_SUCCESS = "single_invite_success"
    SINGLE_INVITE_FAILED = "single_invite_failed"

    BULK_UPLOAD_SUCCESS = "bulk_upload_success"
    BULK_UPLOAD_FAILED = "bulk_upload_failed"
