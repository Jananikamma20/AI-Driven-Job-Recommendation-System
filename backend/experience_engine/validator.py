class ExperienceValidator:

    def __init__(self):
        pass

    def validate(self, records):
        """
        Validate extracted employment records.

        Parameters
        ----------
        records : list
            List of employment records.

        Returns
        -------
        tuple
            (valid_records, invalid_records)
        """

        valid_records = []
        invalid_records = []

        for record in records:

            company = record.get("company")
            designation = record.get("designation")
            start_date = record.get("start_date")
            end_date = record.get("end_date")
            experience = record.get("experience")

            if (
                company is not None
                and designation is not None
                and start_date is not None
                and end_date is not None
                and experience is not None
            ):

                valid_records.append(record)

            else:

                invalid_records.append(record)

        return valid_records, invalid_records