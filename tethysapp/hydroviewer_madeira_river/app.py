from tethys_sdk.base import TethysAppBase, url_map_maker


class HydroviewerMadeiraRiver(TethysAppBase):
    """
    Tethys app class for Hydroviewer: Madeira River.
    """

    name = 'Hydroviewer: Madeira River'
    index = 'hydroviewer_madeira_river:home'
    icon = 'hydroviewer_madeira_river/images/icon.gif'
    package = 'hydroviewer_madeira_river'
    root_url = 'hydroviewer_madeira_river'
    color = '#002255'
    description = ''
    tags = 'geoglows, hydroviewer'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url=f'{self.root_url}',
                controller='hydroviewer_madeira_river.controllers.home'
            ),
            UrlMap(
                name='get_discharge_data',
                url=f'{self.root_url}/get-discharge-data',
                controller='hydroviewer_madeira_river.controllers.get_discharge_data'
            ),
            UrlMap(
                name='get_simulated_data',
                url=f'{self.root_url}/get-simulated-data',
                controller='hydroviewer_madeira_river.controllers.get_simulated_data'
            ),
            UrlMap(
                name='get_simulated_bc_data',
                url=f'{self.root_url}/get-simulated-bc-data',
                controller='hydroviewer_madeira_river.controllers.get_simulated_bc_data'
            ),
            UrlMap(
                name='get_hydrographs',
                url=f'{self.root_url}/get-hydrographs',
                controller='hydroviewer_madeira_river.controllers.get_hydrographs'
            ),
            UrlMap(
                name='get_dailyAverages',
                url=f'{self.root_url}/get-dailyAverages',
                controller='hydroviewer_madeira_river.controllers.get_dailyAverages'
            ),
            UrlMap(
                name='get_monthlyAverages',
                url=f'{self.root_url}/get-monthlyAverages',
                controller='hydroviewer_madeira_river.controllers.get_monthlyAverages'
            ),
            UrlMap(
                name='get_scatterPlot',
                url=f'{self.root_url}/get-scatterPlot',
                controller='hydroviewer_madeira_river.controllers.get_scatterPlot'
            ),
            UrlMap(
                name='get_scatterPlotLogScale',
                url=f'{self.root_url}/get-scatterPlotLogScale',
                controller='hydroviewer_madeira_river.controllers.get_scatterPlotLogScale'
            ),
            UrlMap(
                name='get_volumeAnalysis',
                url=f'{self.root_url}/get-volumeAnalysis',
                controller='hydroviewer_madeira_river.controllers.get_volumeAnalysis'
            ),
            UrlMap(
                name='volume_table_ajax',
                url=f'{self.root_url}/volume-table-ajax',
                controller='hydroviewer_madeira_river.controllers.volume_table_ajax'
            ),
            UrlMap(
                name='make_table_ajax',
                url=f'{self.root_url}/make-table-ajax',
                controller='hydroviewer_madeira_river.controllers.make_table_ajax'
            ),
            UrlMap(
                name='get-time-series',
                url=f'{self.root_url}/get-time-series',
                controller='hydroviewer_madeira_river.controllers.get_time_series'),
            UrlMap(
                name='get-time-series-bc',
                url=f'{self.root_url}/get-time-series-bc',
                controller='hydroviewer_madeira_river.controllers.get_time_series_bc'),
            UrlMap(
                name='get_observed_discharge_csv',
                url=f'{self.root_url}/get-observed-discharge-csv',
                controller='hydroviewer_madeira_river.controllers.get_observed_discharge_csv'
            ),
            UrlMap(
                name='get_simulated_discharge_csv',
                url=f'{self.root_url}/get-simulated-discharge-csv',
                controller='hydroviewer_madeira_river.controllers.get_simulated_discharge_csv'
            ),
            UrlMap(
                name='get_simulated_bc_discharge_csv',
                url=f'{self.root_url}/get-simulated-bc-discharge-csv',
                controller='hydroviewer_madeira_river.controllers.get_simulated_bc_discharge_csv'
            ),
            UrlMap(
                name='get_forecast_data_csv',
                url=f'{self.root_url}/get-forecast-data-csv',
                controller='hydroviewer_madeira_river.controllers.get_forecast_data_csv'
            ),
            UrlMap(
                name='get_forecast_bc_data_csv',
                url=f'{self.root_url}/get-forecast-bc-data-csv',
                controller='hydroviewer_madeira_river.controllers.get_forecast_bc_data_csv'
            ),
        )

        return url_maps
