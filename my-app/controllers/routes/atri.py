import json
from typing import List, Any, Optional
from fastapi import UploadFile
default_state = json.loads('{"Bar1":{"styles":{"width":"","height":"","minWidth":"","minHeight":"","maxWidth":"","maxHeight":"","overflow":""},"custom":{"cartesianGrid":{"show":false,"strokeDasharray":""},"data":[],"xAxis":{"show":false,"key":""},"yAxis":{"show":false},"toolTip":{"show":false},"legend":{"show":false},"stacked":false,"options":{}}}}')
def get_defined_value(state, def_state, key):
	return state[key] if key in state else def_state[key]
class Atri:
	def __init__(self, state: Any):
		self.event_data = None
		self.event_alias = None
		global default_state
		self._setter_access_tracker = {}
		self.Bar1 = state["Bar1"]
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		comp = getattr(self, self.event_alias)
		setattr(comp, callback_name, True)
	@property
	def Bar1(self):
		self._getter_access_tracker["Bar1"] = {}
		return self._Bar1
	@Bar1.setter
	def Bar1(self, new_state):
		self._setter_access_tracker["Bar1"] = {}
		global default_state
		self._Bar1 = BarChart(new_state, default_state["Bar1"])

	def _to_json_fields(self):
		return {
			"Bar1": self._Bar1,
			}


class BarChartstylesClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.width: str = get_defined_value(state, def_state, "width")
		self.height: str = get_defined_value(state, def_state, "height")
		self.minWidth: str = get_defined_value(state, def_state, "minWidth")
		self.minHeight: str = get_defined_value(state, def_state, "minHeight")
		self.maxWidth: str = get_defined_value(state, def_state, "maxWidth")
		self.maxHeight: str = get_defined_value(state, def_state, "maxHeight")
		self.overflow: str = get_defined_value(state, def_state, "overflow")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def width(self):
		self._getter_access_tracker["width"] = {}
		return self._width
	@width.setter
	def width(self, state):
		self._setter_access_tracker["width"] = {}
		self._width = state
	@property
	def height(self):
		self._getter_access_tracker["height"] = {}
		return self._height
	@height.setter
	def height(self, state):
		self._setter_access_tracker["height"] = {}
		self._height = state
	@property
	def minWidth(self):
		self._getter_access_tracker["minWidth"] = {}
		return self._minWidth
	@minWidth.setter
	def minWidth(self, state):
		self._setter_access_tracker["minWidth"] = {}
		self._minWidth = state
	@property
	def minHeight(self):
		self._getter_access_tracker["minHeight"] = {}
		return self._minHeight
	@minHeight.setter
	def minHeight(self, state):
		self._setter_access_tracker["minHeight"] = {}
		self._minHeight = state
	@property
	def maxWidth(self):
		self._getter_access_tracker["maxWidth"] = {}
		return self._maxWidth
	@maxWidth.setter
	def maxWidth(self, state):
		self._setter_access_tracker["maxWidth"] = {}
		self._maxWidth = state
	@property
	def maxHeight(self):
		self._getter_access_tracker["maxHeight"] = {}
		return self._maxHeight
	@maxHeight.setter
	def maxHeight(self, state):
		self._setter_access_tracker["maxHeight"] = {}
		self._maxHeight = state
	@property
	def overflow(self):
		self._getter_access_tracker["overflow"] = {}
		return self._overflow
	@overflow.setter
	def overflow(self, state):
		self._setter_access_tracker["overflow"] = {}
		self._overflow = state
	def _to_json_fields(self):
		return {
			"width": self._width,
			"height": self._height,
			"minWidth": self._minWidth,
			"minHeight": self._minHeight,
			"maxWidth": self._maxWidth,
			"maxHeight": self._maxHeight,
			"overflow": self._overflow,
			}


class BarChartcustomClasscartesianGridClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.show: bool = get_defined_value(state, def_state, "show")
		self.strokeDasharray: str = get_defined_value(state, def_state, "strokeDasharray")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def show(self):
		self._getter_access_tracker["show"] = {}
		return self._show
	@show.setter
	def show(self, state):
		self._setter_access_tracker["show"] = {}
		self._show = state
	@property
	def strokeDasharray(self):
		self._getter_access_tracker["strokeDasharray"] = {}
		return self._strokeDasharray
	@strokeDasharray.setter
	def strokeDasharray(self, state):
		self._setter_access_tracker["strokeDasharray"] = {}
		self._strokeDasharray = state
	def _to_json_fields(self):
		return {
			"show": self._show,
			"strokeDasharray": self._strokeDasharray,
			}


class BarChartcustomClassxAxisClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.show: bool = get_defined_value(state, def_state, "show")
		self.key: str = get_defined_value(state, def_state, "key")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def show(self):
		self._getter_access_tracker["show"] = {}
		return self._show
	@show.setter
	def show(self, state):
		self._setter_access_tracker["show"] = {}
		self._show = state
	@property
	def key(self):
		self._getter_access_tracker["key"] = {}
		return self._key
	@key.setter
	def key(self, state):
		self._setter_access_tracker["key"] = {}
		self._key = state
	def _to_json_fields(self):
		return {
			"show": self._show,
			"key": self._key,
			}


class BarChartcustomClassyAxisClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.show: bool = get_defined_value(state, def_state, "show")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def show(self):
		self._getter_access_tracker["show"] = {}
		return self._show
	@show.setter
	def show(self, state):
		self._setter_access_tracker["show"] = {}
		self._show = state
	def _to_json_fields(self):
		return {
			"show": self._show,
			}


class BarChartcustomClasstoolTipClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.show: bool = get_defined_value(state, def_state, "show")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def show(self):
		self._getter_access_tracker["show"] = {}
		return self._show
	@show.setter
	def show(self, state):
		self._setter_access_tracker["show"] = {}
		self._show = state
	def _to_json_fields(self):
		return {
			"show": self._show,
			}


class BarChartcustomClasslegendClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.show: bool = get_defined_value(state, def_state, "show")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def show(self):
		self._getter_access_tracker["show"] = {}
		return self._show
	@show.setter
	def show(self, state):
		self._setter_access_tracker["show"] = {}
		self._show = state
	def _to_json_fields(self):
		return {
			"show": self._show,
			}


class BarChartcustomClass:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.cartesianGrid: BarChartcustomClasscartesianGridClass = get_defined_value(state, def_state, "cartesianGrid")
		self.data: List[Any] = get_defined_value(state, def_state, "data")
		self.xAxis: BarChartcustomClassxAxisClass = get_defined_value(state, def_state, "xAxis")
		self.yAxis: BarChartcustomClassyAxisClass = get_defined_value(state, def_state, "yAxis")
		self.toolTip: BarChartcustomClasstoolTipClass = get_defined_value(state, def_state, "toolTip")
		self.legend: BarChartcustomClasslegendClass = get_defined_value(state, def_state, "legend")
		self.stacked: bool = get_defined_value(state, def_state, "stacked")
		self.options: dict = get_defined_value(state, def_state, "options")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def cartesianGrid(self):
		self._getter_access_tracker["cartesianGrid"] = {}
		return self._cartesianGrid
	@cartesianGrid.setter
	def cartesianGrid(self, state):
		self._setter_access_tracker["cartesianGrid"] = {}
		self._cartesianGrid = BarChartcustomClasscartesianGridClass(state, self._def_state["cartesianGrid"])
	@property
	def data(self):
		self._getter_access_tracker["data"] = {}
		return self._data
	@data.setter
	def data(self, state):
		self._setter_access_tracker["data"] = {}
		self._data = state
	@property
	def xAxis(self):
		self._getter_access_tracker["xAxis"] = {}
		return self._xAxis
	@xAxis.setter
	def xAxis(self, state):
		self._setter_access_tracker["xAxis"] = {}
		self._xAxis = BarChartcustomClassxAxisClass(state, self._def_state["xAxis"])
	@property
	def yAxis(self):
		self._getter_access_tracker["yAxis"] = {}
		return self._yAxis
	@yAxis.setter
	def yAxis(self, state):
		self._setter_access_tracker["yAxis"] = {}
		self._yAxis = BarChartcustomClassyAxisClass(state, self._def_state["yAxis"])
	@property
	def toolTip(self):
		self._getter_access_tracker["toolTip"] = {}
		return self._toolTip
	@toolTip.setter
	def toolTip(self, state):
		self._setter_access_tracker["toolTip"] = {}
		self._toolTip = BarChartcustomClasstoolTipClass(state, self._def_state["toolTip"])
	@property
	def legend(self):
		self._getter_access_tracker["legend"] = {}
		return self._legend
	@legend.setter
	def legend(self, state):
		self._setter_access_tracker["legend"] = {}
		self._legend = BarChartcustomClasslegendClass(state, self._def_state["legend"])
	@property
	def stacked(self):
		self._getter_access_tracker["stacked"] = {}
		return self._stacked
	@stacked.setter
	def stacked(self, state):
		self._setter_access_tracker["stacked"] = {}
		self._stacked = state
	@property
	def options(self):
		self._getter_access_tracker["options"] = {}
		return self._options
	@options.setter
	def options(self, state):
		self._setter_access_tracker["options"] = {}
		self._options = state
	def _to_json_fields(self):
		return {
			"cartesianGrid": self._cartesianGrid,
			"data": self._data,
			"xAxis": self._xAxis,
			"yAxis": self._yAxis,
			"toolTip": self._toolTip,
			"legend": self._legend,
			"stacked": self._stacked,
			"options": self._options,
			}


class BarChart:
	def __init__(self, state, def_state):
		self._setter_access_tracker = {}
		self._def_state = def_state

		self.styles: BarChartstylesClass = get_defined_value(state, def_state, "styles")
		self.custom: BarChartcustomClass = get_defined_value(state, def_state, "custom")
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}

	@property
	def styles(self):
		self._getter_access_tracker["styles"] = {}
		return self._styles
	@styles.setter
	def styles(self, state):
		self._setter_access_tracker["styles"] = {}
		self._styles = BarChartstylesClass(state, self._def_state["styles"])
	@property
	def custom(self):
		self._getter_access_tracker["custom"] = {}
		return self._custom
	@custom.setter
	def custom(self, state):
		self._setter_access_tracker["custom"] = {}
		self._custom = BarChartcustomClass(state, self._def_state["custom"])
	def _to_json_fields(self):
		return {
			"styles": self._styles,
			"custom": self._custom,
			}

