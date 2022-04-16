<template>
  <div>
    <h4 class="font-weight-bold py-3 mb-4">
      <span class="text-muted font-weight-light">UI elements /</span> Vue Simple Calendar
    </h4>

    <hr class="container-m-nx border-light mt-0 mb-4">

    <!-- New item modal -->
    <b-modal title="Title" ref="newItemModal" @shown="$refs.newItemTitleInput.focus()" @ok.prevent="addItem()" @hidden="clearModal()">
      <form @submit.stop.prevent="addItem()">
        <b-form-group label="Title">
          <b-input v-model="newItemTitle" ref="newItemTitleInput" />
        </b-form-group>
        <b-form-group label="Type">
          <b-form-select v-model="newItemType" :options="[
            { value: '', text: 'Default' },
            { value: 'cv-item-secondary', text: 'Secondary' },
            { value: 'cv-item-success', text: 'Success' },
            { value: 'cv-item-info', text: 'Info' },
            { value: 'cv-item-warning', text: 'Warning' },
            { value: 'cv-item-danger', text: 'Danger' },
            { value: 'cv-item-dark', text: 'Dark' }
          ]" />
        </b-form-group>
      </form>
    </b-modal>
    <!-- / New item modal -->

    <b-card>
      <div class="d-flex">
        <calendar-view class="holiday-us-traditional holiday-us-official" style="min-height: 800px;"
          :items="items"
          :show-date="showDate"
          :time-format-options="{hour: 'numeric', minute:'2-digit'}"
          :display-period-uom="displayPeriodUom"
          :enable-drag-drop="true"
          :show-times="true"
          :display-period-count="1"
          :starting-day-of-week="1"
          locale="en-US"
          item-content-height="1.25rem"
          :displayWeekNumbers="true"
          :enable-date-selection="true"
          :selection-start="selectionStart"
          :selection-end="selectionEnd"
          @date-selection-start="setSelection"
          @date-selection="setSelection"
          @date-selection-finish="finishSelection"
          @drop-on-date="onDrop"
          @click-date="onClickDay"
          @click-item="onClickItem"
          @show-date-change="setShowDate">

          <div slot="header" slot-scope="{ headerProps }" class="d-flex flex-wrap justify-content-center justify-content-md-between align-items-center mb-4">
            <div class="text-large font-weight-light">
              {{ getPeriodLabel(headerProps) }}
            </div>
            <div class="w-100 w-md-auto text-center mt-3 mt-md-0">
              <b-btn-group>
                <b-btn variant="primary" size="sm" :pressed="displayPeriodUom === 'year'" @click="displayPeriodUom = 'year'">Year</b-btn>
                <b-btn variant="primary" size="sm" :pressed="displayPeriodUom === 'month'" @click="displayPeriodUom = 'month'">Month</b-btn>
                <b-btn variant="primary" size="sm" :pressed="displayPeriodUom === 'week'" @click="displayPeriodUom = 'week'">Week</b-btn>
              </b-btn-group>
            </div>
            <div class="w-100 w-md-auto text-center mt-2 mt-md-0">
              <b-btn-toolbar class="d-inline-block">
                <b-btn variant="primary" size="sm" @click="setShowDate(headerProps.currentPeriod)">Today</b-btn>
                <b-btn-group class="ml-1">
                  <b-btn variant="primary icon-btn" size="sm" :disabled="!headerProps.previousYear" @click="setShowDate(headerProps.previousYear)"><i class="ion ion-md-arrow-back scaleX--1-rtl"></i></b-btn>
                  <b-btn variant="primary icon-btn" size="sm" :disabled="!headerProps.previousPeriod" @click="setShowDate(headerProps.previousPeriod)"><i class="ion ion-ios-arrow-back scaleX--1-rtl"></i></b-btn>
                  <b-btn variant="primary icon-btn" size="sm" :disabled="!headerProps.nextPeriod" @click="setShowDate(headerProps.nextPeriod)"><i class="ion ion-ios-arrow-forward scaleX--1-rtl"></i></b-btn>
                  <b-btn variant="primary icon-btn" size="sm" :disabled="!headerProps.nextYear" @click="setShowDate(headerProps.nextYear)"><i class="ion ion-md-arrow-forward scaleX--1-rtl"></i></b-btn>
                </b-btn-group>
              </b-btn-toolbar>
            </div>
          </div>

        </calendar-view>
      </div>
    </b-card>

  </div>
</template>

<style>
  /* Set minimum width */
  .cv-wrapper {
    width: 100%;
    overflow-x: auto;
  }
  .cv-wrapper > * {
    min-width: 600px !important;
  }
</style>

<style src="@/vendor/libs/vue-simple-calendar/vue-simple-calendar.scss" lang="scss"></style>
<style src="vue-simple-calendar/static/css/holidays-us.css" lang="css"></style>

<script>
import { CalendarView, CalendarMathMixin } from 'vue-simple-calendar'

const calendarUtils = CalendarMathMixin.methods

export default {
  name: 'ui-vue-simple-calendar',
  metaInfo: {
    title: 'Vue Simple Calendar - UI elements'
  },
  components: {
    CalendarView
  },
  data: () => ({
    lastItemId: 0,
    showDate: new Date(),
    displayPeriodUom: 'month',

    newItemDate: null,
    newItemTitle: '',
    newItemType: '',

    selectionStart: null,
    selectionEnd: null,

    items: []
  }),
  mounted () {
    this.items = [{
      id: 'e0',
      startDate: '2018-01-05'
    }, {
      id: 'e1',
      startDate: this.thisMonth(15, 18, 30)
    }, {
      id: 'e2',
      startDate: this.thisMonth(15),
      title: 'Single-day item with a long title'
    }, {
      id: 'e3',
      startDate: this.thisMonth(7, 9, 25),
      endDate: this.thisMonth(10, 16, 30),
      class: 'cv-item-info',
      title: 'Multi-day item with a long title and times'
    }, {
      id: 'e4',
      startDate: this.thisMonth(20),
      title: 'My Birthday!',
      classes: 'cv-item-danger',
      url: 'https://en.wikipedia.org/wiki/Birthday'
    }, {
      id: 'e5',
      startDate: this.thisMonth(5),
      endDate: this.thisMonth(12),
      title: 'Multi-day item',
      classes: 'cv-item-success'
    }, {
      id: 'foo',
      startDate: this.thisMonth(29),
      title: 'Same day 1'
    }, {
      id: 'e6',
      startDate: this.thisMonth(29),
      title: 'Same day 2',
      classes: 'cv-item-warning'
    }, {
      id: 'e7',
      startDate: this.thisMonth(29),
      title: 'Same day 3'
    }, {
      id: 'e8',
      startDate: this.thisMonth(29),
      title: 'Same day 4',
      classes: 'cv-item-secondary'
    }, {
      id: 'e9',
      startDate: this.thisMonth(29),
      title: 'Same day 5'
    }, {
      id: 'e10',
      startDate: this.thisMonth(29),
      title: 'Same day 6',
      classes: 'cv-item-dark'
    }, {
      id: 'e11',
      startDate: this.thisMonth(29),
      title: 'Same day 7'
    }]
  },
  methods: {
    thisMonth (d, h = 0, m = 0) {
      const t = new Date()
      return new Date(t.getFullYear(), t.getMonth(), d, h, m)
    },
    setShowDate (d) {
      this.showDate = d
    },
    getPeriodLabel (data) {
      return calendarUtils.formattedPeriod(
        data.periodStart,
        data.periodEnd,
        this.displayPeriodUom,
        data.monthNames
      )
    },
    setSelection (dateRange) {
      this.selectionEnd = dateRange[1]
      this.selectionStart = dateRange[0]
    },
    finishSelection (dateRange) {
      this.setSelection(dateRange)
    },

    onClickDay (d) {
      this.newItemDate = d
      this.$refs.newItemModal.show()
    },
    addItem () {
      if (this.newItemDate && this.newItemTitle) {
        this.items.push({
          id: `ne${this.lastItemId++}`,
          startDate: this.newItemDate,
          title: this.newItemTitle,
          classes: this.newItemType
        })
      }
      this.$nextTick(() => this.$refs.newItemModal.hide())
    },
    clearModal () {
      this.newItemDate = null
      this.newItemTitle = ''
      this.newItemType = ''
    },

    onClickItem (e) {
      alert(`You clicked: ${e.title}`)
    },
    onDrop (item, date) {
      const eLength = calendarUtils.dayDiff(item.startDate, date)
      item.originalItem.startDate = calendarUtils.addDays(item.startDate, eLength)
      item.originalItem.endDate = calendarUtils.addDays(item.endDate, eLength)
    }
  }
}
</script>
